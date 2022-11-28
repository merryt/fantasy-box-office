from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='leagues'),
    path('create', views.create, name='create'),
    path('<int:league_id>/', views.details, name='detail'),
    path('<int:league_id>/t/<int:team_id>/', views.team_detail, name='team_detail'),
]