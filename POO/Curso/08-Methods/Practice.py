class Backpack:
    def __init__(self):
        self._items = []
        
    @property
    def items(self):
        return self._items
    
    def add_items(self, new_item):
        if isinstance(new_item, str):
            self._items.append(new_item)
            
    
    def remove_items(self, what_item):
        if what_item in self._items:
            self._items.remove(what_item)
            
        
        else:
            print(f'No se ha encontrado {what_item}')
        
    def has_items(self, search_item):
        return search_item in self.items
            
        
my_backpack = Backpack()

print(my_backpack.items) #Veo el arreglo

my_backpack.add_items('Lapiz') #Añado algo a la lista
print(my_backpack.items)

print(my_backpack.has_items('Lapiz')) # Imprimo el metodo para ver si existe lapiz en la lista

my_backpack.remove_items('Lapiz') # Remuevo el lapiz del arreglo

print(my_backpack.items)