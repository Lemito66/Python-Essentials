class Coche:
    def __init__(self,marca,modelo,year):
        self.marca=marca
        self.modelo=modelo
        self.year=year
    
    def presentacion(self):
        return f'Su marca es: {self.marca}\nsu modelo es: {self.modelo}\nsu año es: {self.year}'
    
auto_kia=Coche('Chevrolet','Spark',2022)
print(auto_kia.presentacion())

class Acuatico:
    def desplazar(self):
        return f'El animal nada'

class Terrestre:
    def desplazar_terrestre(self):
        return f'El animal es terrestre'

class Cocodrilo(Acuatico,Terrestre):
    pass

cocodrilo=Cocodrilo()
print(cocodrilo.desplazar_terrestre())