# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:20:29 2022

@author: CEC
"""
# Son arreglos que permiten almacenar cualquier tipo de dato
#No todo tipo de dato se puede tranformar en una lista
#Las listas son mutables, string son inmutables
lista=[3,1,2]
#print(len(lista))
#in solo para la lista

for i in lista:    
    print(i)
    
for cadena in "Emiull -Juosusue":
    if cadena=="u":
        continue #Salta a la siguiente repeticion        
    print(cadena)

for cadena in "Emiull -Juosusue":
    if cadena=="u":
        break #Detiene el programa        
    print(cadena)
    
