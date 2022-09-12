class Dog:
    
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
        
    
    def set_name(self, new_name):
        if isinstance(new_name,str) and new_name.isalpha():
            self._name = new_name
            return self._name
        else:
            return f'Nombre no valido'
         
        
my_dog = Dog('Filipo')
print(my_dog.get_name())
print(my_dog.set_name('Kira'))
