# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:33:00 2022

@author: CEC
"""
nombre="Emill"
apellido="Logroño"
edad=24
estatura=1.7
cadena="Saludos, mi nombre es Emill, mi apellido Logroño, \
    tengo 24 años y mi estatura es 1.79 " 
#Primera Forma
print("Saludos, mi nombre es",
      nombre,
      " mi apellido es",
      apellido,
      " tengo",
      edad,
      "años y mi estatura es",
      estatura)
#Segunda Forma
print("Saludos, mi nombre es: "+
      nombre+
      
      " mi apellido "+
      apellido +
      " tengo " +
      str(edad)+
      " años y mi estatura es: "+
      str(estatura))
cadenaTres="Saludos, mi nombre es,%s" %nombre +" y mi apellido es: %s" %apellido
print(cadenaTres)
