'''Realizar un programa que compruebe di el número ingresado es par o impar. Además, compruebe si es múltiplo del 7.
Ejemplo 1:
Ingrese el número a evaluar… 21
El número 21 es impar y SI es múltiplo del 7
Ejemplo 2:
Ingrese el número a evaluar… 16
El número 16 es par y NO es múltiplo de 7
'''
entrada = int(input("Ingrese un numero"))
if entrada%2==0:
    print("Es par")