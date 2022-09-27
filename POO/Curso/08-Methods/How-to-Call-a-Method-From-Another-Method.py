class Backpack:
    
    def __init__(self) -> None:
        self._items = []
        
    @property
    def items(self):
        return self._items
    
    
    
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

my_backpack.add_item('Lapiz')
my_backpack.add_item('Borrador')
my_backpack.add_item('Cartuchera')

print('Not Sorted:')
my_backpack.show_items()

print('Sorted:')
my_backpack.show_items(True)