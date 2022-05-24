# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:01:25 2022

@author: CEC
"""
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:01:25 2022

@author: CEC
"""
def separar(cadena):
    lista=list()
    for i in cadena:
        lista.append(i)
    return lista #Return vacio permite que la funcion ha completado su ejecución
def division(a,b):
    '''
    Funcion para hacer la division

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns a/b
    -------
    TYPE
        DESCRIPTION.

    '''
    if b==0:
        print("Division por cero")
        return
    else:
        return a/b
def ejercicio2():
    '''
    Función que devuelve mi nombre y apellido

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    nombre="Emil"
    apellido="Logroño"
    print(f"Mi nombre es {nombre} y mi apellido es {apellido}")
    return #si esta vacio no retorna nada