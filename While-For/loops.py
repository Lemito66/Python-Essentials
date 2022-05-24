# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:10:36 2022

@author: CEC
"""
'''
Se ejecutan por repeticion
While trabaja con elementos lógicos
While esta diseñada para hacer repeticiones infinitas en python
For tiene repeticiones controladas en base a arreglos.
Todo depende del escenario y la diferencia es la cantidad de repeticiones
El contador es un sistema de control
En python es mejor pedir perdó que pedir permiso
'''
'''Mostrar un mensaje al usuario que le pregunte
al usuario indicandole si quiere que tenga activo
el mensaje, cuando diga no se debe detener la aplicación. '''
# control=0
# while control<=40:
#     print("estructura while", control)
#     control +=2
#mensaje=input("Ingrese Si o No")
'''contador=1
while contador<2:
    mensaje=input("Ingrese Si o No: ")
    if mensaje.lower()=="no":
        contador=3'''
#continue salta una sola repeticion y continua a la siguiente
#break detiene 
while True:
    mensaje=input("Ingrese Si o No: ")
    if mensaje.lower()=="no":
        break #El break solo funciona cuando se cumple el if
        
    

    