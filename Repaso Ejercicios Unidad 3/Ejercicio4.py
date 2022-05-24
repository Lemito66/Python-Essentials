# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:17:52 2022

@author: CEC
"""
''' 4. Se necesita una aplicación que clasifique a las personas según
sus rangos de edad en diferentes grupos.
15 años adolescente
15-25 años: jóven adulto
25 años: adulto '''

edad = int(input("Ingrese su edad: "))
if edad <=15:
    print("Es Adolescente")
elif edad >25:
    print("Es un adulto")
else:
    print("Es un joven adulto")
# if edad >= 0 and edad <= 3:
#     print("Usted es un bebe")
# elif edad >= 4 and edad <= 12:
#     print("Usted es un niño")
# elif edad >= 12 and edad <= 17:
#     print("Usted es adolescente")
# elif edad >= 18 and edad <= 64:
#     print("Usted es mayor de edad")
# elif edad >= 65 and edad <= 200:
#     print("Usted es de la tercera edad")
# else:
#     print("Edad invalida!")