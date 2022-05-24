# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:58:45 2022

@author: CEC
Todo en python es un objeto y se lo crea por plantillas
Esa clase es un objeto
Las clases definen las caracteristicas generales y especificas de los objetos
Se necesita instanciar, y eso significa que nos permita crear una plantilla 
para crear esos objetos
Una clase debe tener atributos, objetos

Self es para referirnos a los atributos de esa clase

Las clases hijas recibe los atributos, metodos, instancias todo de la clase padre
"""

class Humano():
    def __init__(self,edad,estatura,nombre,apellido):#Init es una variable de entorno general, que iniciliza las caracteristicas propias de la clase
        self.edad=edad
        self.estatura=estatura
        self.nombre=nombre
        self.apellido=apellido
    def presentacion(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nEstatura: {self.estatura}")
    def lista(self,genero,etnia): #Estos atributos solo es para el metodo, no para el objeto
        self.genero=genero
        self.etnia=etnia
        print(f"[{self.genero},{self.etnia},{self.nombre},{self.apellido},{self.edad},{self.estatura}]")
#Con presentación
# darleAtributos=Humano(24,1.87,"Emill")
# type(darleAtributos)     
# darleAtributos=Humano(24,1.87,"Emill","Logroño")
# darleAtributos.presentacion()  
#Con la lista
# darleAtributo=Humano(24,1.87,"Emill","Logroño") 
# darleAtributo.lista("mASCULINO","Indigena")
