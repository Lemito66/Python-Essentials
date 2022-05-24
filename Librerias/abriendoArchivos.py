# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:27:10 2022

@author: CEC
"""
archivo=open(r"C:\Users\CEC\Desktop\texto.txt")#Una Forma
archivoDos=open("C:\\Users\\CEC\\Desktop\\texto.txt",encoding="utf-8")#Otra Forma
archivo.readline()
archivo.readlines()
archivoTres=open("C:\\Users\\CEC\\Desktop\\texto.txt","r",encoding="utf-8")#La r es solo modo lectura
#Como la quito de modo lectura
archivoTres=open("C:\\Users\\CEC\\Desktop\\texto.txt","a",encoding="utf-8")#La a es para quitar modo lectura
archivoTres.write("Esto es nuevo texto") #Esto es para añadir al archivo
'''Aunque se añade texto si revisamos en el documento no se guarda,
para eso debemos cerrar el archivo y de ahi si se carga las palabras '''
archivoTres.close()

archivoTres=open("C:\\Users\\CEC\\Desktop\\texto.txt","w",encoding="utf-8")# w Remplazo 
