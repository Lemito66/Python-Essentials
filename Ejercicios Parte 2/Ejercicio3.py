# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:04:31 2022

@author: CEC
Se necesita una aplicación que muestre un menú con tres
opciones: “1. Comenzar programa, 2. Mostrar segundo mensaje,
3. Finalizar programa”. El usuario debe poder seleccionar una
opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del
error. El menú se debe volver a mostrar luego de ejecutada cada
opción excepto en la opción 3, se interrumpirá la impresión del
menú y el programa finalizará.
"""
while True:
    entrada=(input("1 Comenzar programa\n2. Mostrar segundo mensaje\n3. Finalizar programa\n"))
    if entrada =="3":
        print("Se acabo el programa")
        break
    elif entrada =="2":
        print("Hola")
    elif entrada =="1":
        print("Comenzamos el programa")
    else:
        print("No ha digitado una opción incorrecta")
