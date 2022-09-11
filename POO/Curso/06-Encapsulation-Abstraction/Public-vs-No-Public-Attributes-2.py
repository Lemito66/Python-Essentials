class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa
    
student_emill = Student('1','Emill Logroño', 24, 10)
try:
    print(student_emill._age)
except(AttributeError):
    print('Hubo un error my brow')
    
class Backpack:
    def __init__(self):
        self._items = []
        
my_backpack = Backpack()
print(my_backpack._items)

class Movie:
    id_counter = 1
    
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating
        self._id = Movie.id_counter
        Movie.id_counter +=1
        
my_movie = Movie('Spiderman',2004, 10)
your_movie = Movie('Ironman',2009, 6)

print(my_movie._id)
print(your_movie._id)