from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='leagues'),
    path('<int:movie_id>/', views.details, name='detail'),
]