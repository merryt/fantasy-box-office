from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from users.models import User, Player
from league.models import Team, League
import datetime
from django.contrib import messages


def is_movie_in_league(league_id, movie_id):
    
    teams_in_league = Team.objects.filter(league=league_id)
    movies_in_league = []
    for team in teams_in_league:
        for movie in team.movie_picks.all():
            movies_in_league.append(movie.id)

    if movie_id in movies_in_league:
        return True
    else:
        return False

def details(request, movie_id):
    current_movie = get_object_or_404(Movie, pk=movie_id)
    current_player = Player.objects.get(auth_user_link=request.user.id)
    related_teams = Team.objects.filter(player=current_player.id)
    only_one_team = related_teams.count() == 1
    is_movie_on_team = False
    
    if(only_one_team):
        team = related_teams.first()
        is_movie_on_team = team.movie_picks.filter(id=movie_id).count() >= 1


    context = { "movie" : current_movie, "only_one_team": only_one_team, "is_movie_on_team":is_movie_on_team, "related_teams":related_teams}
    if request.method == 'POST':
        if 'remove_movie' in request.POST:
            team.movie_picks.remove(current_movie)
            team.save()
            context["is_movie_on_team"] = False
        
        elif 'add_movie' in request.POST:
            if(team.movie_picks.all().count() > 6):
                context["picks_error"] = "ooooph, to many picks, remove one to continue"
                return render(request, 'movies/details.html', context)
            team.movie_picks.add(current_movie)
            team.save()
            context["is_movie_on_team"] = True
        elif 'add_movie_to_team' in request.POST:
            team_id = request.POST['add_movie_to_team']
            target_team = related_teams.get(id=team_id)
            this_league = target_team.league
            movie_already_in_league = is_movie_in_league(this_league.id, movie_id)
            movie_already_on_team = (target_team.movie_picks.filter(id=movie_id).count() != 0)
                      
            if movie_already_on_team:
                messages.error(request, 'This team already has that movie')
            elif movie_already_in_league:
                messages.error(request, 'someone else already has it')  
            else:
                target_team.movie_picks.add(current_movie)
                target_team.save()
                

            
            
    return render(request, 'movies/details.html', context)

def index(request):
    context = { "upcoming_movies": Movie.objects.filter(release_date__gte=datetime.date.today()).order_by('release_date') }
    return render(request,'movies/index.html', context)

def rules(request):
    context = {}
    return render(request,'movies/rules.html', context)

def remove(request, movie_id, team_id, league_id ):
    current_player = Player.objects.get(auth_user_link=request.user.id)
    team = Team.objects.get(id=team_id)
    if (team.player.id == current_player.id ):
        current_movie = get_object_or_404(Movie, pk=movie_id)
        team.movie_picks.remove(current_movie)
        team.save()
    
    
    return redirect(f'/l/{league_id}/t/{team_id}')