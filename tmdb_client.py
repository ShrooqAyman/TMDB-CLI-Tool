import requests
from config import TMDB_API_KEY, TMDB_API_URL

def fetch_movies(category):
    """
    Fetches a list of movies from The Movie Database (TMDB) API based on the specified category.

    Parameters:
        category (str): The movie category to fetch. Examples include:
            - 'popular'
            - 'top_rated'
            - 'upcoming'
            - 'now_playing'

    Returns:
        list: A list of movie dictionaries if the request is successful.
              Returns an empty list if there is an error.
    """

    url = f"{TMDB_API_URL}{category}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []
