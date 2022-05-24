# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:37:04 2022

@author: CEC
"""
# 1-10 niño
# 11-20 adolescente
#21-35 joven adulto
#36-50 adulto
#51- ---- adulto mayor
edad = int(input("Ingrese su edad: "))
if edad >= 1 and edad <= 10:
    print("Usted es un niño")
elif edad <= 20:
    print("Usted es un adolescente")
elif edad <= 35:
    print("Usted es joven adulto")
elif edad <= 50:
    print("Usted es adulto")
else:
    print("Adulto mayor")
