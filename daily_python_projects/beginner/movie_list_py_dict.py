# Project Description
# Create a program that starts with a predefined list of your favorite movies. For example:
from symtable import Class

# Initial list of favorite movies
class MovieList:
    # intialize the favorite Movie list
    def __init__(self, movie_list):
        self.favorite_movies = movie_list

    def add_movie(self,new_movie):
        self.favorite_movies.append(new_movie)
        return self

    def remove_movie(self, movie_name):
        favorite_movies.remove(movie_name)
        return self

    def sorted_list(self):
        return

    def disply_movie_list(self):
        for movie in self.favorite_movies:
            print(f"- {movie}")

if __name__ == "__main__":
    favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    my_favorite_movie = MovieList(favorite_movies)
    # my_favorite_movie.disply_movie_list()
    # my_favorite_movie.add_movie("The Hoidays").disply_movie_list()
    my_favorite_movie.add_movie("Test Movie").remove_movie("Inception").disply_movie_list()

