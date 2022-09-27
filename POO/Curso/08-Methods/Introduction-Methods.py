class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def find_diameter(self):
        return f'Diameter {self.radius * 2}'
    
my_circle = Circle(5)

diameter = my_circle.find_diameter()
print(diameter)
print(my_circle.find_diameter())