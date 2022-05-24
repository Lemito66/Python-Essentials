# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:24:19 2022

@author: CEC
"""
#complex permite cambia parte real a imaginaria
variableUno=5.8888
print(complex(variableUno,2)) 
#round permite redondear
print(round(5.88))
#Cadenas
cadena="Hola Emill"
print(cadena[0])#Imprime el primer elemento de la cadena
#Funcion len permite saber la logitud de la cadena
print(len(cadena))
#Poner comillas simples dentro de comillas
cadenaUno="Haciendo pruebas en un entorno 'Python' 3.0"
#Poner comillas dobles dentro de comillas simples
cadenaDos='Segunda prueba en "Spyder"'
#Otra Forma
cadenaTres="Tercera prueba de \"Python\" en \"Spyder\""
#Visualizar el indice
print(cadenaUno[0])
cadenaCuatro = cadenaUno[13]
print(cadenaCuatro)
#Visualizar la primera palabra
print(cadenaUno[0:8])
#Desde la posicion hasta el final
print(cadenaDos[-8:])
#Desde el inicio hasta 8
print(cadenaDos[:8])
#Primeras dos palabras
print(cadenaTres[0:14])
#De uno en uno
print(cadenaTres[0:14:1])
#De dos en dos
print(cadenaTres[0:14:2])
#Las cadenas no se pueden modificar
animalesUno="Perro"
animalesDos="Gato"
animalesTres="Gallina"
print(animalesUno+animalesDos+animalesTres)
print("Perro"+"Gato"+"Gallina")

#Saber la longitud
print(len(animalesUno))
#x.count()retorna el numero de veces que se repite un caracter en la cadena.
print(animalesUno.count("u",))
# x.upper(): devuelve una copia de la cadena convirtiendo las letras minúsculas en mayúsculas.
print(animalesUno.upper())
# x.lower(): devuelve una copia de la cadena convirtiendo las letras mayúsculas a minúsculas.
print(animalesUno.lower())
# x.capitalize() coloca solo el primer carácter en mayúscula
print(animalesUno.capitalize())
#Los metodos son funciones especiales para un tipo de dato en especial
#Las funciones trabajan para distintas cosas
# x.title(): devuelve una copia de la cadena usando la notación de título
print(animalesUno.title())
# x.replace(anterior, nuevo): devuelve una copia de la cadena a la cual se le ha cambiado la primera
# ocurrencia del carácter especificado uno nuevo
print(animalesUno.replace("r", "P"))
# x.lstrip(): devuelve una copia de la cadena a la cual se le han eliminado los espacios del principio.
cadenaSesis="                 Centro                 "
print(cadenaSesis.lstrip())
#x.rstrip(): devuelve una copia de la cadena a la cual se le han eliminado los espacios del final.
print(cadenaSesis.rstrip())

# x.split(sep=None): devuelve una lista de las palabras de la cadena separadas acorde al parámetro sep.
print(cadenaSesis.split())
cadenaSiete="lemito66@gmail.com"
print(cadenaSiete.split("@")) #Separamos el @
cadenaOcho=cadenaUno.split()
# .join (x) devuelve la unión de los caracteres del string usando un nuevo carácter específicado
print("3".join(cadenaOcho))
###
cadenaNueve="Inclusión de backslash dentro de un string\\ Aqui\\"
print(cadenaNueve)
cadenaDiez="Primera line \n Segunda Linea"
#Salto de linea \n
print(cadenaDiez)
#Tabulacion \t
cadenaDiez="Primera line \t Segunda Linea"
print(cadenaDiez)
#Retorno del cursor
cadenaDiez="Primera line \r Segunda Linea"
print(cadenaDiez)