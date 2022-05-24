# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:01:40 2022

@author: CEC
Se necesita una aplicación que permita encontrar el promedio de
“n” valores ingresados por teclado.

"""
#primerNumero=int(input("Ingrese el primer número: "))
lista = []
promedio = 0
while True:
    primerNumero = int(input("Ingrese un número: "))
    lista.append(primerNumero)
    aprobacionONegacion = int(
        input("1. Ver promedio\n2.Seguir Digitando\n3.Parar:\n"))
    if aprobacionONegacion == 1:
        promedio = sum(tuple(lista))/len(lista)
        print(promedio)
        break
    elif aprobacionONegacion == 3:
        break


# print(lista)


# segundoNumero=int(input("Ingrese el segundo número: "))
# print(f"El promedio es {(primerNumero+segundoNumero)/2}")
