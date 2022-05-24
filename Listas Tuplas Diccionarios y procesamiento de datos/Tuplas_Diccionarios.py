# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:23:31 2022

@author: CEC
"""

#Tuplas con parentesis. Las tuplas son inmutales, las listas si
tupla=(1,2,3)
print(tupla)
#Diccionarios con llaves, son objetos mutables, son estrutura de datos
#Son mas importantes que las lista
#Los elementos no estan indexados 
#Se lo llama mediante su key
#La diferencia es en el tiempo de buscado, es mejor en diccionario

diccionario={"Nombre":"Emil","Apellido":"Logroño"}
print(diccionario["Apellido"])
print(diccionario["Apellido"])
#Los arreglos internos de un Diccionario si estan indexados
print(diccionario["Apellido"][0])