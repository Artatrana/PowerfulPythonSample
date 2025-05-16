# Favourite Movie list with decorator
# Decorators
def log_method_call(func):
    """Logs the method name and arguments whenever it is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__} with args: {args[1:]}, kwargs: {kwargs}")
        return func(*args,**kwargs)
    return wrapper

def validate_movie_name(func):
    """Ensures movie names are strings and non-empty before executing."""
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, str) or not arg.strip():
                raise ValueError("Movie name must be a non-empty string.")
        return func(self, *args, **kwargs)

    return wrapper

# MovieList Class
class MovieList:
    def __init__(self, movie_list):
        """Initialize the favorite movie list."""
        self.favorite_movies = movie_list

    @log_method_call
    @validate_movie_name
    def add_movie(self, movie_name):
        """Add a new movie to the list."""
        self.favorite_movies.append(movie_name)
        return self

    @log_method_call
    @validate_movie_name
    def remove_movie(self, movie_name):
        """Remove a movie from the list by name."""
        if movie_name in self.favorite_movies:
            self.favorite_movies.remove(movie_name)
        else:
            print(f"Movie '{movie_name}' not found in the list.")
        return self

    @log_method_call
    def sorted_list(self):
        """Return the list of movies sorted alphabetically."""
        return sorted(self.favorite_movies)

    @log_method_call
    def disply_movie_list(self):
        """Display the current list of favorite movies."""
        print("Favorite Movies:")
        for movie in self.favorite_movies:
            print(f"- {movie}")

if __name__ == "__main__":
    favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    my_favorite_movie = MovieList(favorite_movies)

    # Chain method calls with logging and validation
    my_favorite_movie.add_movie("The Holidays").remove_movie("Inception").disply_movie_list()

    # Demonstrate sorted list
    print("\nSorted Movie List:")
    print(my_favorite_movie.sorted_list())
