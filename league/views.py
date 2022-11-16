from django.shortcuts import render
from django.http import HttpResponse 
from .models import League

def index(request):
    return HttpResponse("list of all leagues")

def details(request, league_id):
    current_league = League.objects.get(pk=league_id)
    print(current_league)
    return HttpResponse(f'you are looking at leauge: {current_league.name}')

