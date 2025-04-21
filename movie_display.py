def print_movies(movies):
    """
    Prints a formatted list of movies to the terminal.

    Parameters:
        movies (list): A list of movie dictionaries, each containing details
                       like 'title', 'release_date', and 'vote_average'.
    """
    for movie in movies[:10]:  # Display first 10 results
        title = movie.get("title", "No title")
        release_date = movie.get("release_date", "N/A")
        rating = movie.get("vote_average", "N/A")
        print(f"{title} - ({release_date}) - Rating: {rating}")
