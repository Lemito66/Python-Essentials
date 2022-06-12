""" •	EJERCICIO 1:
Escriba un programa que genere una tabla de multiplicar del número que ingrese el usuario, el número de veces que se imprimirán las operaciones también lo debe establecer el usuario.
Ejemplo:
Número para realizar las tablas… 7
Hasta qué número… 5
7 X 0 = 0
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
"""
try:
    tablaDel = int(input("Ingrse el numero para realizar las tablas: "))
    hastaQueNumero = int(input("Hasta que número: "))
    for i in range(hastaQueNumero+1):
        print(f"{tablaDel} * {i} = {tablaDel*i}")
except(ValueError):
    print("Error")