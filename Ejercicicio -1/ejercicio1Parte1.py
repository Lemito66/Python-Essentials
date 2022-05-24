# Parte 1
''' Crear un código sencillo capaz de mostrar en pantalla lo siguiente:
Empezando a trabajar con Python
Realizado por: “Emill Logroño”
Consultando los tipos de valores:
El tipo de dato de 875 es:
SALIDA
El tipo de dato de 4.89 es:
SALIDA
El tipo de dato del texto: Now is better than never. es:
SALIDA
El tipo de dato de 1.32 es:
SALIDA
¿El valor 5 + 8i corresponde a un valor entero?
SALIDA
¿El valor 8.2 corresponde a un valor entero?
SALIDA
¿El texto: Readability counts. corresponde a un string?
SALIDA '''
#Type nos permite saber que tipo de dato es por ejemplo: int, float, complex, str.
print("El tipo de dato de 875 es:")
print(type(875))
print("El tipo de dato de 4.89 es:")
print(type(4.89))
print("El tipo de dato del texto: Now is better than never. es:")
print(type("Now is better than never."))
print("El tipo de dato de 1.32 es:")
print(type(1.32))
#insistance : Esta es una función nativa en Python desde la versión 3.5, permite hacer una comparación de datos y tipo de datos.
print("¿El valor 5 + 8i corresponde a un valor entero?")
print(isinstance(5+8,int))
print("¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(8.2,int))
print("¿El texto: Readability counts. corresponde a un string?")
print(isinstance("Readability counts. corresponde a un string?",str))

