from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='leagues'),
    path('create', views.create, name='league_create'),
    path('<int:league_id>/', views.details, name='league_details'),
    path('<int:league_id>/t/<int:team_id>/', views.team_detail, name='team_details'),
]