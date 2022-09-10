class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
my_circle = Circle(5, 'Red')

print(my_circle.radius)
print(my_circle.color)

my_circle.radius = 8
my_circle.color = 'Green'

print(my_circle.radius)
print(my_circle.color)