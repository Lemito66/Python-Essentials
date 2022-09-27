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
my_backpack = Backpack()

my_backpack.add_item('Lapiz')
#my_backpack.remove_item('Lapiz')
print(my_backpack.has_item('Lapiz'))

my_backpack.add_item('Sleeping Backpack')
print(my_backpack._items)

has_water = my_backpack.has_item('Lapiz')
print(has_water)

my_backpack.remove_item('Lapiz')
print(my_backpack.items)