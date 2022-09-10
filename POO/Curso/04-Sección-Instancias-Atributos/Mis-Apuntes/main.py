#Crear clase
class Backpack:
    def __init__(self, peso, color):
        self.items = []
        self.color = color
        self.peso = peso
        
    def presentacion(self):
        return f'El color es: {self.color} y el peso es: {self.peso}'
    
#Definir clases
class Circle:
    def __init__(self, radius):
        self.radiues = radius
        self.color = 'Blue'
        
class Rectangule:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Movie:
    def __init_(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

darle_atributos = Backpack(55, 'red')
print(darle_atributos.presentacion())