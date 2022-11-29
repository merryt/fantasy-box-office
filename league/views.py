from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import League, Team
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
            Team.objects.filter(league=current_league).filter(player = request.user.id).delete()
            current_league.teams.remove(request.user.id)
            return redirect(f'/l/{league_id}')  
        
        elif 'league_join' in request.POST:
            team_name = request.POST["team_name"]
            team = Team.objects.create(team_name=team_name, player=Player.objects.get(auth_user_link=request.user.id), league=current_league)
            team.save()            

            return redirect(f'/l/{league_id}')  

    current_teams = Team.objects.filter(league=current_league)
    context = { 
               "current_league" : current_league, 
               "teams": current_teams,
               "is_active_user_in_leauge": current_teams.filter(player = request.user.id).exists()
               }
    return render(request, 'league/details.html', context)


def team_detail(request, league_id, team_id):
    team = Team.objects.get(pk=team_id)
    print(team)
    context = {
        "team": team,
    }
    return render(request, 'league/team.html', context)

def my_leagues(request):
    myteams = Team.objects.filter(player=request.user.id)
    context = {
        "teams": myteams,
    }
    return render(request, 'league/myleagues.html', context)