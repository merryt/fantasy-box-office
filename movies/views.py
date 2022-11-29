from django.shortcuts import render, get_object_or_404
from .models import Movie
from users.models import User
from league.models import Team
import datetime



def details(request, movie_id):
    current_movie = get_object_or_404(Movie, pk=movie_id)
    related_teams = Team.objects.filter(player=request.user.id)
    only_one_team = related_teams.count() == 1

    # todo: build "select for team" logic
    # todo: figure out if this movie is already on that players team
    if request.method == 'POST':
        if(only_one_team):
            related_teams.first().movie_picks.add(current_movie)
            related_teams.first().save()
            print(related_teams.first().movie_picks)
    context = { "movie" : current_movie, "only_one_team": only_one_team }
    return render(request, 'movies/details.html', context)

def index(request):
    context = { "upcoming_movies": Movie.objects.filter(release_date__gte=datetime.date.today()).order_by('release_date') }
    return render(request,'movies/index.html', context)