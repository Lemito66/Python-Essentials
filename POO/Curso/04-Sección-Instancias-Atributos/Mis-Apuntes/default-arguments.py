class Circle:
    def __init__(self, radius=5, color):#No se debe poner un argunmento despues de que se le asigna un valor a otro
        self.radius = radius
        self.color = color
        
my_circle = Circle('Red')
print(my_circle.radius)
print(my_circle.color)

class Circle:
    def __init__(self, color, radius=5 ):#Esto si funciona
        self.radius = radius
        self.color = color
        
my_circle = Circle('Red')
print(my_circle.radius)
print(my_circle.color)

