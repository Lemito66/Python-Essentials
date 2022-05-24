# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:58:06 2022

@author: CEC
"""
diccionario={"Nombres":"EMILL","Apellidos":"Logroño ","key1":[1,2,3,4]}
print(diccionario["key1"][2])
for dic in diccionario:
    print(f"Key {dic} {diccionario[dic]}")
#Zip crea pares entre los que encuentre, va a necesitar una funcion constructora
zip=("higgo",[1,5,7,4,8,20],"texto")
print(list(zip))
#print(dict(zip))
#items le transforma a tupla con key y valor
#diccionarioTres=dict(zip("higgo",[5,55,"texto","hola",6]))
#print(diccionarioTres)
#keys devuelve el keys
#value devuelve una lista por valores
#clear limpia todos los elementos del diccionario
#Los diccionarios al ser mutables no ocupan el mismo espacio de memoria
#copy nos devulve una copia nueva
##hacer una busqueda
diccionario.get("Apellidos")
#update remplaza cuando no hay nada parecido
#y si no existe se remplaza
#Update agrega esos elementos que no existen y actualiza esos valores que se repiten
