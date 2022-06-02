import random 
import string 
listaMinisculas=(list(string.ascii_lowercase))
listaMayusculas=(list(string.ascii_uppercase))
listaNumeros=(list(string.digits))
listaCompleta=listaMinisculas+listaMinisculas+listaNumeros
for i in range(10):
    listaLetras=list()
    for i in range(6):
        escogerLetra=random.choice(listaCompleta)
        listaLetras.append(escogerLetra)
    textoCompleto=''.join(listaLetras)
    print(textoCompleto)




