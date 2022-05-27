'''Parte 1
Considerando la siguiente tupla codifique un programa que permita separar los números pares
e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.
Datos_2021 = [1, 2, 3, ,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]'''
Datos_2021 = [1, 2, 3, 5, 4, 5, 6, 7, 100, 91, 110,
              900, 21, 33, 32, 2, 4, 8, 10, 13, 13, 16, 15, 1302]
Datos_2021 = tuple(Datos_2021)
entrada = int(input("1. Numeros pares\n2. Numeros impares\n"))
for i in Datos_2021:
    if entrada == 1:
        if i % 2 == 0:
            print(f"{i} es par")
    elif entrada == 2:
        if i % 2 != 0:
            print(f"{i} es impar")
    # print(i)

