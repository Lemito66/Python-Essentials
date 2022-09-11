class Backpack:
    def __init__(self,name):
        self.__items = ['Book','Pencil']
        self.name = name
        
    def __presentacion(self):
        return f'El nombre de su maleta pero privado: {self.name}'
    
    def presentacion_normal(self):
        return f'El nombre de su maleta pero publico: {self.name}'
        
my_backpack = Backpack('Lemito')

#Para acceder debemos poner el nombre de la clase con un guion bajo y el doble guion en el atributo
print(my_backpack._Backpack__items)
print(my_backpack._Backpack__presentacion())
print(my_backpack.presentacion_normal())