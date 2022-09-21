from typing_extensions import Self


class BouncyBall:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self.brand = brand
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price >0:
            self._price = new_price
        else:
            print('Ingresa un precio correcto')
            
    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if isinstance(new_size, str) and new_size.isalpha():
            self._size = new_size
            
        else:
            print('Ingresa una talla correcta')
            
    size = property(get_size, set_size)




my_bouncy_ball = BouncyBall(8.5,'M','Nike')

print(my_bouncy_ball.price)

my_bouncy_ball.price = 8.0
print(my_bouncy_ball.price)

print(my_bouncy_ball.size)
my_bouncy_ball.size = 'L'
print(my_bouncy_ball.size)


class Dog:
    
    def __init__(self, name, age) -> None:
        
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
            
        else:
            print('Ingrese un nombre correcto')
            
my_dog = Dog('Filipo', 5)

print(my_dog.name)

my_dog.name = 'Kira'
print(f'My new dog is {my_dog.name}')

print(my_dog._age)