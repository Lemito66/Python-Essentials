class Backpack:
    max_num_items = 10
    
    def __init__(self):
        self.items = []
        
    def ingresar_elemento(self, numero):
        self.numero = numero
        self.items.append(self.numero)
        return self.items
        



print(Backpack.max_num_items)

my_backpack = Backpack()
print(my_backpack.max_num_items)

Backpack.max_num_items = 15
print(Backpack.max_num_items)
print(my_backpack.max_num_items)

for i in range(1,20):
    my_backpack.ingresar_elemento(i)

print(my_backpack.items)