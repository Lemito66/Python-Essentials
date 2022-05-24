# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:05:08 2022

@author: CEC

Crear un string y recorrer con un while
"""
cadena="abcdefghik"
control=0
while control<len(cadena):
    print(cadena[control],end="")
    control+=1
else:#Si no entra en el while unicamente incluye el else
#Si se ejecuta el while al ultimo ejecuta el else.
    print("Se acabo\n")