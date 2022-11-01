class Backpack:
    
    def __init__(self) -> None:
        self._items = []
        
    @property
    def items(self):
        return self._items
    
    #Como usar metodos dentro de otro metodo
    #self.nombreMetodo()
    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item) # Usamos el metodo add_item para añadir un item
            
    def remove_multiple_items(self, items):
        for item in items:
            if item in self._items:
                self.remove_item(item) # Usamos el metodo remove_item para remover item
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Please provide a valid item.')
            
    def remove_item(self, item):
        if isinstance(item, str) and item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('No se ha encontrado valores iguales')
            return 0
        
    def has_item(self, item):
        return item in self._items 
    
    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))#Sorted ordena de forma ascendente en este caso, reverse=True
        else:
            print(self._items)
my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_multiple_items(['Lapiz', 'Candy','Chocolate'])
print(my_backpack.items)

my_backpack.remove_multiple_items(['Lapiz', 'Candy'])
print(my_backpack.items)