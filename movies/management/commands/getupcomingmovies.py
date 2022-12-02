from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
import requests
import json
from movies.models import Movie
import datetime
import re

load_dotenv()



def get_movies(current_page = 0):
    today = datetime.date.today() 
    one_year_from_today = f'{datetime.date.today().year + 1}-{datetime.date.today().month}-{datetime.date.today().strftime("%d")}'
    
    
    #this is currently set to only run for the US region
    
    if(current_page == 0 ):
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={os.environ["TMDB_KEY"]}&language=en-US&sort_by=release_date.asc&primary_release_date.gte={today}&primary_release_date.lte={one_year_from_today}&region=US'
    else:
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={os.environ["TMDB_KEY"]}&language=en-US&sort_by=release_date.asc&primary_release_date.gte={today}&primary_release_date.lte={one_year_from_today}&region=US&page={current_page}'
   
    # url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={os.environ["TMDB_KEY"]}'
    
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
        
    try: 
        results = json.loads(response.text)["results"]
    except:
        return "An error occurred getting the movie results form the api call"
    
    
    if (len(results)== 0):
        print(results)
        return current_page
    else:    
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
        return get_movies(current_page + 1)

class Command(BaseCommand):
    help = 'Use this command to get all the upcoming movies'


    def handle(self, *args, **options):
    
        pages_of_movies_pulled = get_movies()
        
        self.stdout.write(self.style.SUCCESS(f'no errors is probably a good thing, we pulled {pages_of_movies_pulled} pages of movies from TMDB... so like {pages_of_movies_pulled*20} or so'))
        pass
    
    