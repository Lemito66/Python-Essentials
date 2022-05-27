# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:34:20 2022

@author: CEC
"""
'''Aplicacion que permita contar la 
cantidad de vocales dentro de una frase'''
lista=["a","e","i","o","u"]
frase="Hola"
# print(range(0,5))
# print(list(range(5)))
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador
for i in frase:
    print(i)
print(contar_vocales("Emiiiiill"))
    