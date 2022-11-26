from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
import requests
import json
from movies.models import Movie
import datetime
import re

load_dotenv()


class Command(BaseCommand):
    help = 'Use this command to get all the upcoming movies'

    def handle(self, *args, **options):
        
        url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={os.environ["TMDB_KEY"]}'
        
        try:
            response = requests.request("GET", url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)
        
        
        
        results = json.loads(response.text)["results"]
        
        
        
        if (len(results)== 0):
            self.stdout.write(self.style.ERROR(f'SHOOT, NO MOVIES FROM TMDB'))
        for movie in results:
            release_date_arr = [int(x) for x in movie["release_date"].split("-")]                    
            release_date_fmt = datetime.date(*release_date_arr)
            Movie.objects.update_or_create(
                     id=movie["id"],
                     defaults = {
                        "backdrop_path": movie["backdrop_path"],
                        "original_title": movie["original_title"],
                        "title": movie["title"],
                        "original_language": movie["original_language"],
                        "overview": movie["overview"],                     
                        "popularity": movie["popularity"],                     
                        "poster_path": movie["poster_path"],                     
                        "release_date": release_date_fmt,    
                     }                 
            )

        self.stdout.write(self.style.SUCCESS(f'no errors is probably a good thing, we pulled {len(results)} movies from TMDB'))
        pass
    
    