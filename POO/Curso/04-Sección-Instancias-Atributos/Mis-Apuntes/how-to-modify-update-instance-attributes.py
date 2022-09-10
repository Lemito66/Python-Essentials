class Backpack:
    def __init__(self, color):
        self.items = []
        self.color = color
        
my_backpack = Backpack('Blue')
your_backpack = Backpack('Green')
print(my_backpack.color)
print(your_backpack.color)

print('Changing Color....')
my_backpack.color = 'Red'
your_backpack.color = 'Yellow'
print(my_backpack.color)
print(your_backpack.color)

print(my_backpack.items)
palabra = 'Hola'
for i in palabra:
    my_backpack.items.append(i)
    
print(my_backpack.items)



class Casa:
    def __init__(self,precio):
        self.precio = precio
        
    def comparando_precios(self):
        if self.precio > 225:
            return f'Es un buen precio'
        else:
            return f'Pesimo precio'
    
    
my_house = Casa(225)
print(f'El valor de mi casa ahora es de {my_house.precio}')

print('Cambiando valores')
my_house.precio = 230
print(f'El valor de mi casa despues de unos años será de {my_house.precio}')

print(my_house.comparando_precios())
