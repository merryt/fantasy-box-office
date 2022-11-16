from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import League

def index(request):
    number_of_leauges = League.objects.count()
    return HttpResponse(f'There are {number_of_leauges} leagues')

def details(request, league_id):
    current_league =get_object_or_404(League, pk=league_id)
    print(current_league)
    return HttpResponse(f'you are looking at leauge: {current_league.name}')

