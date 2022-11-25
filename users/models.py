from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

class Player(models.Model):
    auth_user_link = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players" 


    def __str__(self):
        auth_user = get_object_or_404(User, pk=self.auth_user_link.id)
        return auth_user.username
    
    
    
    
