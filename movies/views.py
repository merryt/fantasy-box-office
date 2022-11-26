from django.shortcuts import render, get_object_or_404
from .models import Movie

def details(request, movie_id):
    current_movie = get_object_or_404(Movie, pk=movie_id)
    context = { "current_movie" : current_movie, }
    return render(request, 'movies/details.html', context)

def index(request):
    context = { "upcoming_movies": Movie.objects.all().order_by('release_date') }
    return render(request,'movies/index.html', context)