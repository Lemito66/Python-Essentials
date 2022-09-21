class Dog:
    
    def __init__(self, age):
        self._age = age
        
    def get_age(self):
        print('Calling the getter')
        return self._age
    
    def set_age(self, new_age):
        print('Calling the setter')
        if isinstance(new_age, int) and 0 < new_age < 30: 
            self._age = new_age
        else:
            print('Plase enter a valid age.')
            
    age = property(get_age, set_age)
        
my_dog = Dog(8)

#We can use the same sintax to acces and modify the attributes with property
print(f'My dog is {my_dog.age} years old.')
print('One year later...')

my_dog.age +=1
print(f'My dog is now {my_dog.age} years old.')

class Persona:
    
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print('Ingrese un nombre valido')
            
    name = property(get_name, set_name)
    
my_name = Persona('Emill')
print(my_name.name)#Emill

my_name.set_name('Manuel')
print(my_name.get_name())#Manuel
print(my_name.name)#Manuel