from dotenv import load_dotenv
import os

load_dotenv()

TMDB_API_KEY = os.getenv('TMDB_API_KEY')  
TMDB_API_URL = "https://api.themoviedb.org/3/movie/"
