# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:44:44 2022

@author: CEC
"""
def multiplicarN(*valores): 
    lista=list(valores)
    resultado=1
    for i in lista:
        resultado= resultado*i
    return resultado
print(multiplicarN(1,2))

# def multiplicarNWhile(*valores): 
#     lista=list(valores)
#     resultado=1
#     i=0
#     while i<len(lista):
#         resultado*=lista[i]
#     return resultado
#print(multiplicarNWhile(5,5,5,5,5,5,5))
def ejemplo(par1,par2=20,*par3):
    print(par1)
    print(par1)
    print(par3)