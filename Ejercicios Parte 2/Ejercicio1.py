# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:59:35 2022

@author: CEC
1. Se necesita una aplicación que mantenga activo una pregunta en
pantalla hasta que se ingrese mediante teclado la palabra “NO”,
entonces se terminará el programa.
"""
while True:
    entrada=input("Ingrese Si o No: ")
    if entrada.lower()=="no":
        break