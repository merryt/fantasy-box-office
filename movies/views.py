from django.shortcuts import render
from .models import Movie


def details(request):
    return render(request,'movies/detail.html')

def index(request):
    context = { "upcoming_movies": Movie.objects.all().order_by('release_date') }
    return render(request,'movies/index.html', context)