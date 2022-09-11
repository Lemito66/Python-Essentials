#Public Attributes
class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
my_car = Car('Kia','Picanto',2023)

print(my_car.year)

my_car.year = 5600

print(my_car.year)

# No Public Attributes, but onlye de attribute year
class Truck:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year
        
my_truck = Truck('Hino','Mavesa',2023)

print(my_truck._year)#Así se puede visualizar 

my_truck._year = 2024 #Así modificar

print(my_truck._year)# Así imprimirlo de nuevo

