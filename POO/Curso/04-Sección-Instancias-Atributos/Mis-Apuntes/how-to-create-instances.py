class Backpack:
    def __init__(self):
        self.items = []

#Crear instancias sin argumentos        
my_backpack = Backpack()
print(my_backpack)

#One Arguments
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
my_circle = Circle(5.5)
print(my_circle)

#Multiple Arguments
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
my_rectangle = Rectangle(5, 5.5)
print(my_rectangle)