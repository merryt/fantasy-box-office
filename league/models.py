from django.db import models
from users.models import Player
from movies.models import Movie

class League(models.Model):
    name = models.CharField(max_length=128)
    teams = models.ManyToManyField(Player)
    
    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    team_name = models.CharField(max_length=128)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    movie_picks = models.ManyToManyField(Movie)
    def __str__(self):
        return f'{self.team_name}'
