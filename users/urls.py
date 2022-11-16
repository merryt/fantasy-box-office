from django.urls import path

from . import views

urlpatterns = [
    path('<int:player_id>/', views.profile, name='profile'),
]