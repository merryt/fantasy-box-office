from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import League
from users.models import Player
from django.contrib.auth.decorators import login_required

from django.core import serializers


def index(request):
    context = { "number_of_leagues": League.objects.count(), "list_of_leagues": League.objects.all() }
    return render(request,'league/index.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST['name']

        if League.objects.filter(name=name).exists():
            error = "Name alrady Taken"
            return render(request,'league/create.html',{'error':error})
        else:
            league = League.objects.create(name=name)
            league.save()
            return redirect('leagues')        
    
    return render(request,'league/create.html')


def details(request, league_id):    
    current_league = get_object_or_404(League, pk=league_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        if 'league_leave' in request.POST:
            current_league.players.remove(request.user.id)
            return redirect(f'/l/{league_id}')  
        
        elif 'league_join' in request.POST:
            current_league.players.add(request.user.id)
            current_league.save()

            return redirect(f'/l/{league_id}')  

    context = { "current_league" : current_league}
    return render(request, 'league/details.html', context)
