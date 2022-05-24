# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:17:35 2022

@author: CEC
Lista dentro de otra lista
"""
listaUno=[1,5,46,9,8,[5,8,9],8,6,5]
print(listaUno[5])
tupla=(1,8,9,6,3,4,7,6)#Tuplas y cadenas son inmutables
#Hacer lista a una tupla

print(list(tupla))
#tupla a lista
print(tuple(listaUno))

##sorted ordena una nueva lista
tuplaDos=(1,99,4,6,3,2,6,8,7,5,3,5)
print(sorted(tuplaDos))
#min el minimo devuelve un solo valor
print(min(tuplaDos))
#max el maximo devuelve un solo valor
print(max(tuplaDos))
#index retorna la posicion en la lista del elemento especificado
print(tuplaDos.index(3))
#count devuelve cuanta cantida existe
print(tuplaDos.count(5))

#sum suma todo
print(sum(tuplaDos))
#in hace busquedas en listas,tuplas y strings




