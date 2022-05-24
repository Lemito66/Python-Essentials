# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:41:01 2022

@author: CEC
"""
import numpy as np
# dir("numpy") para ayuda
sample_list = [1, 2, 3]
listaEnNumpy=np.array([5,9,7,6,2,3,1])
listaDosEnNumpy=np.array([1,5,9,7,6,2,3])

#print(type(listaEnNumpy)) #Tipo de dato
# print(np.array(sample_list)) #imprimiendo la lista
#print(listaEnNumpy+listaDosEnNumpy)#Suma matriz

#Crear una matriz
#matriz=np.array([45,"A",4,56],[8,"B",6,4],[9,"L",9,3],[98,"A"])#Debe ser del mismo tipo y aqui esta mal
#print(matriz)
matrizDos=np.array([[45,"A",4,56],[8,"B",6,4],[9,"L",9,3],[98,"A"]])
#matrizDos=np.array(matrizDos)

#print(matrizDos)
variableRandom=np.arange(5, 100)
print(variableRandom)
#matriz de 0 
matrizCero=np.zeros(10)
print(matrizCero)
