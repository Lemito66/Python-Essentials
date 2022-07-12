class Acuatico:
    def desplazar(self):
        return(f'El animal nada')
    
class Terrestre:
    def desplazar(self):
        return (f'El animal anda')

class Cocodrilo(Terrestre,Acuatico):
    pass

cocodrile=Cocodrilo()
print(cocodrile.desplazar())