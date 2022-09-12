class Movie:
    
    def __init__(self, title, rating, year):
        self._title = title
        self._rating = rating
        self.__year = year
    
    #Get    
    def get_title(self):
        return self._title
    #Set
    def set_title(self , name):
        self._title = name
        return self._title
    
    

my_movie = Movie('Spiderman',10, 2008)
print(my_movie._rating)


print(my_movie.get_title())
print(my_movie.set_title('Spiderman 2'))

my_movie._rating = 5
print(my_movie._rating)

print(my_movie._Movie__year)
my_movie._Movie__year = 2022
print(my_movie._Movie__year)