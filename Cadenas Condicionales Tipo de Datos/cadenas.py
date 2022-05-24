# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:21:07 2022

@author: CEC
"""
nombre="Emill"
apellido="Logroño"
edad=24
estatura=1.7
cadena="Saludos, mi nombre es %s, mi apellido es %s, \
mi estatura es: %s , y mi edad es %s"%(nombre,
apellido,
edad,
estatura)#Se trabaja de esta forma
                                                      
#print(cadena)
#Metodo Format
cadenaDos="Saludos, mi nombre es {0}, mi apellido es {1},\
mi edad es {2} y mi estatura es: {3}".format(
nombre,apellido,edad,estatura)
cadenaTres="hola {}".format("Jorge")
cadenaCuatro="Hola {variableUno}".format(variableUno="Emill")
#cadenaCinco="Hola {variableUno}".format(variableUno=input("Ingrese su nombre"))
# print(cadenaTres)
# print(cadenaCuatro)
# print(cadenaCinco)
#Cadenas Tipo F, puede ir F mayuscula o f miniscula
cadenaTipoF=f"Saludos, mi nombre es {nombre} , mi apellido es {apellido.upper()} ,\
mi edad es {edad}  y mi estatura es {estatura}"

#print(cadenaTipoF)
#Cadena tipo row o cadena indefinida, no va a interpretar nada osea una doble interpretación
cadenaTipoRow = cadenaTipoF
cadenaTipoRow = r"Saludos, mi nombre es {nombre} , mi apellido es {apellido.upper()} ,\
mi edad es {edad}  y mi estatura es {estatura}"
print(cadenaTipoRow)