from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='leagues'),
    path('create', views.create, name='create'),
    path('<int:league_id>/', views.details, name='detail'),
]