# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:39:58 2022

@author: CEC
"""
a,b=15,0
'''
try:
    print(a/b)#Intenta hacer este codigo
except (ZeroDivisionError,TypeError):#Esto se ejecuta cuando hay error
    print("Division")
else:#else esta ligado a try
    print("Esto esta dentro del else")
finally:#finally siempre se va a ejecutar, esta ligado tambien cuando error
    print("Esto esta dentro de finally")'''
    
edad=input("Ingrese su edad")
try:
    print(f"{int(edad)}")
    
except (TypeError,ValueError):
    print("Error")
    
    