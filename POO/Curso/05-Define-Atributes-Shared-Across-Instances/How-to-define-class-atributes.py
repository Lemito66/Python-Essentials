# <class_attribute> = <value>
class Dog:
    #class atribute, not using self
    species = 'Canis Lupus'
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
class Backpack:
    
    max_num_items = 10
    
    def __init__(self):
        self.items = []