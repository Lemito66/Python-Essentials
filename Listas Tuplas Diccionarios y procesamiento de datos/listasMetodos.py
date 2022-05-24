# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:23:31 2022

@author: CEC
"""

#Las funciones son bloques de codigo con un nombre asociado
#Que reciben cero o más argumentos como entrada
listaUno=[1,2,3,4,5,6,7,"Emill","Jossue"]
listaTres=[var1 for var1 in range(10)]
#print(listaTres)
#append añade un unico elemento a la lista, y siempre se agrega al final
listaUno.append("Jossue")
listaUno.append(["Jossue",1,2,3])
#print(listaUno)
#print(listaUno[2][1])
#Extend permite agregar elementos al final de la lista, solo se puede agregar un tipo de dato
listaUno.extend("ansdf")
print(listaUno)
#insert nos permite agregar un elemento sobre una lista en una posicion especifica
listaUno.insert(2, "texto")
print(listaUno)
# del es una funcion elimina un elemento
del(listaUno[2])
print(listaUno)
#Vaciar lista igualando a list
listaUno=list()
print(listaUno)
#Remove busca la primera coincidencia y luego la elimina, SOLO LA PRIMERA
listaUno=[1,2,3,4,5]
listaUno.remove(3)
print(listaUno)
#reverse permite dar la vuelta 
listaUno.reverse()
print(listaUno)
#sorted ordenar asc o desc
nuevaLista=[1,5,9,3,7,8,6,4,3,2,4]
nuevaLista.sort()#menor a mayor
print(nuevaLista)
nuevaLista.sort(reverse=True)#Mayor a menor

print(nuevaLista)
#Ahora con strings
lista6=["D","a","ff","aa"]
lista6.sort()#Ordena alfabeticamente pero tiene privilegios en numeros,mayuscula,minusculas
print(lista6)
#
lista8=["34","T","d"]
lista8.sort()
print(lista8)