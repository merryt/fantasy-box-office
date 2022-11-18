from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import League

def index(request):
    context = { "number_of_leauges": League.objects.count()   }
    return render(request,'league/index.html', context)

def create(request):
    return render(request,'league/create.html')


def details(request, league_id):
    current_league =get_object_or_404(League, pk=league_id)
    print(current_league)
    return HttpResponse(f'you are looking at leauge: {current_league.name}')

