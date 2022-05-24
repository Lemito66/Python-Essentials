# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:02:36 2022

@author: CEC
"""
''' Una aplicacion que muestre los numero del 1 al 10
debe saltarse el numero 6'''
'''
contador=1
while contador<=10:
    if contador==6:
        contador+=1
    print(contador)
    contador +=1 '''
#Continue solo deja realizar un una repeticion
#El continue hace el salto de una repetición
#Se salta una de las repeticiones en ese punto y vuelve a realizar la repetición
#Se salta la que coindice con esa repetición
contador=1
while contador<=10:
    if contador==6:
        contador+=1
        continue
    print(contador)
    contador+=1
