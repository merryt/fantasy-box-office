from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='leagues'),
    path('<int:league_id>/', views.details, name='detail'),
]