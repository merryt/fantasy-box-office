from django.db import models
from users.models import Player

class League(models.Model):
    name = models.CharField(max_length=128)
    players = models.ManyToManyField(Player)
    
    def __str__(self):
        return f'{self.name}'


    