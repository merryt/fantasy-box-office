from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movie_id>/', views.details, name='movie_detail'),
    path('remove/<int:movie_id>/<int:team_id>/<int:league_id>/', views.remove, name="remove_movie"),
]