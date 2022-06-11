
def sumaNumeros(cuantosNumeros):
    listaNumeros=list()
    for i in range(cuantosNumeros):
        try:
            numero=int(input(f"Ingresa el número {i+1}: "))
            listaNumeros.append(numero)
        except(ValueError):
            return "Error"      
    return sum(listaNumeros)
print(sumaNumeros(2))