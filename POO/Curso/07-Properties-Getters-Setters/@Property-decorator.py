from doctest import ELLIPSIS_MARKER


class Movie:
    
    def __init__(self, title, rating):
        self.tittle = title
        self._rating = rating
        
    @property#Getter
    def rating(self):
        print('Calling the getter')
        return self._rating
    
    @rating.setter#Setter
    def rating(self, new_rating):
        print('Calling the setter')
        if isinstance(new_rating, float) and 1.0 <= new_rating <=5.0:
            self._rating = new_rating
        else:
            print('Please enter a valid rating.')
    
favorite_movie = Movie('Titanic', 10)
print(favorite_movie.rating)

favorite_movie.rating = 5.0
print(favorite_movie.rating)

 
class Dog:
    
    def __init__(self, name):
        self._name = name 
        
    @property#Getter
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print('Enter a name valid')
            
my_dog = Dog('Filipo')
print(my_dog.name)

my_dog.name = 'Kira'
print(my_dog.name)