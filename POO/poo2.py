class Coche():
    def __init__(self, gasolina):
        self.gasolina = gasolina

    def arrancar(self):
        if self.gasolina > 0:
            print('Arranca')
        else:
            print('No arranca')
        
    def presentacion(self):
        return(f'Usted tiene {self.gasolina} litros de gasolina')

    def conducir(self):
        if self.gasolina >0:
            self.gasolina -=1
            print(f'Quedan,{self.gasolina}, litros')
        else:
            print('No se mueve')

darle_atributos=Coche(5)
#print(darle_atributos.presentacion())
#print(darle_atributos.conducir())
#print(darle_atributos.arrancar())

class OtroCoche():
    def __init__(self, marca, modelo, year):
        self.marca=marca
        self.modelo=modelo
        self.year=year
        
    def presentacion(self):
        return(f'Su marca es: {self.marca}\nSu modelo es: {self.modelo}\nSu año es: {self.year}')

darle_atributos_OtroCoche=OtroCoche('Kia','Picanto','2023')
print(darle_atributos_OtroCoche.presentacion())