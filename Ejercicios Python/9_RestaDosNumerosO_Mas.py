def restaNumeros(cuantosNumeros):
    listaNumeros=list()
    resta=0
    for i in range(cuantosNumeros):
        try:
            numero=int(input(f"Ingresa el número {i+1}: "))
            #listaNumeros.append(numero)
            resta=numero-resta
        except(ValueError):
            return "Error"      
    return resta
print(restaNumeros(2))