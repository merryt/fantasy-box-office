from django.shortcuts import render, get_object_or_404
from .models import Movie
import datetime


def details(request, movie_id):
    current_movie = get_object_or_404(Movie, pk=movie_id)
    context = { "movie" : current_movie, }
    return render(request, 'movies/details.html', context)

def index(request):
    context = { "upcoming_movies": Movie.objects.filter(release_date__gte=datetime.date.today()).order_by('release_date') }
    return render(request,'movies/index.html', context)