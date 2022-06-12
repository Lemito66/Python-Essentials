""" Realice un programa que pida al usuario un número del 1 al 24 y que retorne el nombre de la provincia ecuatoriana cuyo código de la cédula coincida con el número ingresado. Debe ser a prueba de usuarios en sentido de que, si se ingresa un número fuera del rango dado, el programa no debe caerse y deba imprimir el error.
Ejemplo 1:
Ingrese el código (del 1 al 24) … 27
ERROR: Valor fuera del rango.
Ejemplo 2:
Ingrese el código (del 1 al 24) … 17
El código “17” pertenece a la provincia Pichincha.
"""
try:
    entrada = int(input("Ingrese un número del 1 al 24: "))
    if entrada == 1:
        print("Su provincia es Azuay")
    elif entrada == 2:
        print("Su provincia es Bolívar")
    elif entrada == 3:
        print("Su provincia es Cañar")
    elif entrada == 4:
        print("Su provincia es Carchi")
    elif entrada == 5:
        print("Su provincia es Chimborazo")
    elif entrada == 6:
        print("Su provincia es Cotopaxi")
    elif entrada == 7:
        print("Su provincia es El Oro")
    elif entrada == 8:
        print("Su provincia es Esmeraldas")
    elif entrada == 9:
        print("Su provincia es Galápagos")
    elif entrada == 10:
        print("Su provincia es Guayas")
    elif entrada == 11:
        print("Su provincia es Imbabura")
    elif entrada == 12:
        print("Su provincia es Loja")
    elif entrada == 13:
        print("Su provincia es Los Ríos")
    elif entrada == 14:
        print("Su provincia es Manabí")
    elif entrada == 15:
        print("Su provincia es Morona-Santiago")
    elif entrada == 16:
        print("Su provincia es Napo")
    elif entrada == 17:
        print("Su provincia es Orellana")
    elif entrada == 18:
        print("Su provincia es Pastaza")
    elif entrada == 19:
        print("Su provincia es Pichincha")
    elif entrada == 20:
        print("Su provincia es Santa Elena")
    elif entrada == 21:
        print("Su provincia es Santo Domingo de los Tsáchilas")
    elif entrada == 22:
        print("Su provincia es Sucumbíos")
    elif entrada == 23:
        print("Su provincia es Tungurahua")
    elif entrada == 24:
        print("Su provincia es Zamora-Chinchipe")
    else:
        print("Solo debe ingresar un numero del 1 al 24")
except(ValueError):
    print("Error")

