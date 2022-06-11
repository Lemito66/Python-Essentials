'''Realizar un programa que compruebe di el número ingresado es par o impar. Además, compruebe si es múltiplo del 7.
Ejemplo 1:
Ingrese el número a evaluar… 21
El número 21 es impar y SI es múltiplo del 7
Ejemplo 2:
Ingrese el número a evaluar… 16
El número 16 es par y NO es múltiplo de 7
'''
entrada = int(input("Ingrese un numero: "))
if entrada%2==0 and entrada%7==0:
    print(f"El numero {entrada} es par y si es multiplo de 7")
elif entrada%2==0 and entrada%7!=0:
    print(f"El numero {entrada} es par y no es multiplo de 7")
elif entrada%2!=0 and entrada%7==0:
    print(f"El numero {entrada} es impar y si es multiplo de 7")
else:
    print(f"El numero {entrada} es impar y no es multiplo de 7")