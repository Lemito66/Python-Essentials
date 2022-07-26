# -*- coding: utf-8 -*-
class Emill():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.data=[]
    
    def presentacion(self):
        return f'Tu nombre es: {self.nombre} y tu apellido es: {self.apellido}'
    
    def add(self,x):
        self.data.append(x)
#lista=[]
""" dato = Emill('J','D')
lista= dato.add('J')

print(lista) """

class Alumnos():
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.lista=[]
    
    
def dar_nombre_apellido():
    liste=[]
    resultado=''
    name=Alumnos()
    name.nombre=input('Ingresa tu nombre: ')
    name.apellido=input('Ingresa tu apellido')
    name.lista= liste.append(name.nombre)
    # resultado += f'{name.nombre} {name.apellido}'
    resultado = name.lista
    return resultado

print(dar_nombre_apellido())




