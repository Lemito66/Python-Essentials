'''si el nombre comienza con dos guiones bajos (y no termina
también con dos guiones bajos) se trata de una variable o función privada, en caso contrario es pública. Los métodos cuyo nombre comienza y termina con dos guiones bajos son métodos especiales que Python
llama automáticamente bajo ciertas circunstancias'''
class Ejemplo:
    def publico(self):
        return(f'Publico')
    
    def __privado(self):
        return(f'Privado')

mostrar=Ejemplo()
print(mostrar.publico())
#print(mostrar.__privado())#Asi no se puede ingresar
print(mostrar._Ejemplo__privado())#Asi, si se puede
