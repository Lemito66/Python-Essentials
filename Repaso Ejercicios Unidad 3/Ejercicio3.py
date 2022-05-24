# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:47:08 2022

@author: CEC
"""
''' 3. Se necesita una aplicación que devuelva el menor de dos
números ingresados. '''
numeroUno = int(input("Ingrese el primer número: "))
numeroDos = int(input("Ingrese el segundo número: "))
numeroTres = int(input("Ingrese el tercer número: "))
if numeroUno < numeroDos and numeroUno <numeroTres:
    print(numeroUno," Es menor")
elif numeroDos < numeroUno and numeroDos <numeroTres:
    print(numeroDos, " Es menor")
elif numeroTres < numeroUno and numeroTres <numeroDos:
    print(numeroTres," Es menor")
else:
    print("Son iguales")