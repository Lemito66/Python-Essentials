#Modify class attributes
#<ClassName>.<class_attribute> = <new_value>
class Dog:
    id_contador = 1
    
    def __init__(self, name):
        self.name = name
        self.id = Dog.id_contador
        
        Dog.id_contador +=1
        
my_dog = Dog('Filipo')
your_dog = Dog('Kira')


print(my_dog.id)
print(your_dog.id)

class Circle:
    radiues = 5
    
    def __init__(self, color):
        self.color = color
        
print('Class Radiues')      
print(Circle.radiues)

my_circle = Circle('Blue')
your_circle = Circle('Red')

print(my_circle.radiues)
print(your_circle.radiues)

Circle.radiues = 10
print('Change')
print(Circle.radiues)
my_circle.radiues=22
print(my_circle.radiues)
your_circle.radiues = 50
print(your_circle.radiues)

class Pizza:
    
    price=5
    
    def __init__(self,name):
        self.name = name
    
my_favourite_pizza = Pizza('Pepperoni')
my_favourite_pizza.price = 9
print(my_favourite_pizza.price)

Pizza.price = 14.50
your_favourite_pizza = Pizza('Marguerita')
print(your_favourite_pizza.price)