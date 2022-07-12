'''Hay tres conceptos que son básicos para cualquier lenguaje de programación orientado a objetos: el encapsulamiento, la herencia y el
polimorfismo.'''

class Instrumento():
    def __init__(self,precio):
        self.precio=precio
    
    def tocar(self):
        mensaje=f'Estamos tocando musica'
        return mensaje
    
    def romper(self):
        mensaje= f'Eso lo pagas tu! \n Son ${self.precio}'
        return mensaje

'''Como Bateria y Guitarra heredan de Instrumento, ambos tienen un
método tocar() y un método romper(), y se inicializan pasando un
parámetro precio. Pero, ¿qué ocurriría si quisiéramos especificar un
nuevo parámetro tipo_cuerda a la hora de crear un objeto Guitarra?
Bastaría con escribir un nuevo método __init__ para la clase Guitarra
que se ejecutaría en lugar del __init__ de Instrumento. Esto es lo que
se conoce como sobreescribir métodos'''

'''Ahora bien, puede ocurrir en algunos casos que necesitemos sobreescribir un método de la clase padre, pero que en ese método queramos
ejecutar el método de la clase padre porque nuestro nuevo método no
necesite más que ejecutar un par de nuevas instrucciones extra. En ese
caso usaríamos la sintaxis SuperClase.metodo(self, args) para llamar
al método de igual nombre de la clase padre. Por ejemplo, para llamar
al método __init__ de Instrumento desde Guitarra usaríamos Instrumento.__init__(self, precio)'''

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass