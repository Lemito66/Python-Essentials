# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:40:57 2022

@author: CEC
"""
def tablaDelNueve():
    cadena=""
    for i in range(13):
        cadena+=f"9 * {i} = {9*i}\n"
    return cadena
print(tablaDelNueve())
'''
Esto en la consola
archivoTres=open("C:\\Users\\CEC\\Desktop\\texto.txt","w",encoding="utf-8")# w Remplazo 
archivoTres.write(tablaDelNueve())
archivoTres.close()'''

'''
Esto para crear un archivo word y luego poder trabajarlo
archivoTres=open("C:\\Users\\CEC\\Desktop\\doc.docx","w",encoding="utf-8")# w Remplazo
'''