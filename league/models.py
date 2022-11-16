from django.db import models

class League(models.Model):
    name = models.CharField(max_length=128)
    
    # list of all players in this leauge   
    # players = models.ManyToManyField(Players)
    
    def __str__(self):
        return f'{self.name}'


    