class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating
        
favorite_movie = Movie('Spiderman',2008,'Español',5)
your_favorite_movie = Movie('If I Stay',2012,'Español',5)

print('My Favorite Movie')
print(favorite_movie.title)
print(favorite_movie.year)
print(favorite_movie.language)
print(favorite_movie.rating)

print('Your favorite movie')
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)