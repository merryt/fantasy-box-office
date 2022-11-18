from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    nickname = models.CharField(max_length = 150, blank = True, null = True, unique = False)
    groups = None
    user_permissions = None
    
    # todo, password is kinda wonky in django admin


    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players" 


    def __str__(self):
        return self.username
    
    
    
    
    
