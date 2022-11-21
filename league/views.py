from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import League

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
        # add user to this leauge. 
        print(current_league)
        return redirect('leagues')  
    
    context = { "current_league" : current_league}
    return render(request, 'league/details.html', context)
