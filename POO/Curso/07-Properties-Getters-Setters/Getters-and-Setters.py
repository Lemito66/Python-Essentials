class Backpack:
    
    def __init__(self):
        self._items = []
        
    def get_items(self):
        return self._items
    
    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please enter a valid list of items.')
            
            
my_backpack = Backpack()

print(my_backpack.get_items())

my_backpack.set_items(['Pencil', 'Sleeping Bag','First Aid Kit'])
#my_backpack.set_items('Hola')#This is not correct because only take list 
print(my_backpack.get_items())