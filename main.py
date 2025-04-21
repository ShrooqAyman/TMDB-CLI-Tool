import argparse
from tmdb_client import fetch_movies
from movie_display import print_movies

def main():
    """
    Entry point for the TMDB CLI application.

    Parses command-line arguments to determine the type of movies the user wants to see and fetches data from TMDB accordingly.

    Supported types:
        --type popular   -> Popular movies
        --type top       -> Top-rated movies
        --type upcoming  -> Upcoming movies
        --type playing   -> Now playing movies
    """
    parser = argparse.ArgumentParser(description="TMDB CLI")
    parser.add_argument('--type', choices=['popular', 'top', 'upcoming', 'playing'], required=True,
                        help="Type of movies")
    args = parser.parse_args()

    movie_type_map = {
        'popular': 'popular',
        'top': 'top_rated',
        'upcoming': 'upcoming',
        'playing': 'now_playing'
    }

    movies = fetch_movies(movie_type_map[args.type])
    print_movies(movies)

if __name__ == "__main__":
    main()
