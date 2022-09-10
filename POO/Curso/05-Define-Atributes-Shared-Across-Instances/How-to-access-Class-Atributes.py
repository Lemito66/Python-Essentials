# <ClassName>.<classAtribute>
class Dog:
    #class atribute, not using self
    species = 'Canis Lupus'
    id_counter = 1
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        #Inside the class <ClassName>.<classAtribute>
        self.id = Dog.id_counter
        
        Dog.id_counter +=1
        
#print(Dog.species)
my_dog = Dog('Filipo',3,'Akita')
your_dog = Dog('Kira',1,'Akita')
print(my_dog.id)#1
print(your_dog.id)#2

class Movie:
    contador = 1
    def __init__(self, name, rating):
        self.id = Movie.contador
        self.name = name
        self.rating = rating
        
        Movie.contador +=1
        
my_movie = Movie('Spiderman',5)
print(my_movie.id)

class Backpack:
    max_num_items = 10
    
    def  __init__(self):
        self.items = []

my_backpack = Backpack()
your_backpack = Backpack()
#Access Class Atributes
print('Backpack Class')
print(Backpack.max_num_items)
print(my_backpack.max_num_items)
print(your_backpack.max_num_items)