from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256)
    overview = models.TextField()
    original_title = models.CharField(max_length=256)
    original_language = models.CharField(max_length=32)
    backdrop_path = models.CharField(max_length=256, blank=True, default=None, null=True,)
    popularity = models.FloatField(blank=True, default=None)
    poster_path = models.CharField(max_length=256,blank=True, default=None, null=True,)
    release_date = models.DateField()
    id = models.PositiveIntegerField(primary_key=True)
    
    def __str__(self):
        return f'{self.title} - {self.id}'

