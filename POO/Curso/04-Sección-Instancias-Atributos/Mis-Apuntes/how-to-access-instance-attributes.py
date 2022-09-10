#<object>.<attribute>

class Backpack:
    def __init__(self):
        self.items = []
        self.palabra = 'Hola'
        for i in self.palabra:
            self.items.append(i)
        print(self.items)
        
my_backpack = Backpack()
print(my_backpack.items)