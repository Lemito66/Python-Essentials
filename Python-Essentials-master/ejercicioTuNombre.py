# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:14:08 2022

@author: CEC
"""
'''
Pedir nombre, apellido, su edad, y su estatura
Se necesita una aplicacion que se consulte 4 cosas, una vez que se tenga esos datos,:
    Saludo mi nombre es: salto de linea:
        mi apellido es: 
            nombre y apellido la primera como mayuscula
            Tercera su edad y cuarta estatura
            en la ultima se concatena todo '''

# nombre,apellido,edad,estatura=input("Ingresa tu nombre \n"),input("Ingresa tu apellido \n"),input("Ingresa tu edad \n"),input("Ingresa tu estatura\n")
# print(nombre,apellido,edad,estatura) Otra Forma
nombre=input("Ingresa tu nombre \n")
apellido=input("Ingresa tu apellido \n")
edad=input("Ingresa tu edad \n")
estatura=input("Ingresa tu estatura\n")
# primerSaludo=f"Hola, tu nombre es {nombre.capitalize()}\n\
# tu apellido es:{apellido.capitalize()} \ntu edad es {edad.capitalize()} \n\
# y tu estatura es {estatura.capitalize()}"
# segundoSaludo=f"Hola, tu nombre es {nombre.capitalize()}, \
# tu apellido es: {apellido.capitalize()} tu edad es {edad.capitalize()} \
# y tu estatura es {estatura.capitalize()}"
# print(primerSaludo)
# print(segundoSaludo)
print(f"Hola, tu nombre es {nombre.capitalize()}\n\
tu apellido es:{apellido.capitalize()} \ntu edad es {edad.capitalize()} \n\
y tu estatura es {estatura.capitalize()}\n\
Hola, tu nombre es {nombre.capitalize()}, \
tu apellido es: {apellido.capitalize()} tu edad es {edad.capitalize()} \
y tu estatura es {estatura.capitalize()}")

