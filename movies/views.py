from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from users.models import User
from league.models import Team
import datetime



def details(request, movie_id):
    current_movie = get_object_or_404(Movie, pk=movie_id)
    related_teams = Team.objects.filter(player=request.user.id)
    only_one_team = related_teams.count() == 1
    is_movie_on_team = False
    
    if(only_one_team):
        team = related_teams.first()
        is_movie_on_team = team.movie_picks.filter(id=movie_id).count() >= 1

    # todo: build "select for team" logic
    
    if request.method == 'POST':
        if 'remove_movie' in request.POST:
            team.movie_picks.remove(current_movie)
            team.save()
            is_movie_on_team = False
        
        elif 'add_movie' in request.POST:
            team.movie_picks.add(current_movie)
            team.save()
            is_movie_on_team = True  
            
    context = { "movie" : current_movie, "only_one_team": only_one_team, "is_movie_on_team":is_movie_on_team, }
    return render(request, 'movies/details.html', context)

def index(request):
    context = { "upcoming_movies": Movie.objects.filter(release_date__gte=datetime.date.today()).order_by('release_date') }
    return render(request,'movies/index.html', context)