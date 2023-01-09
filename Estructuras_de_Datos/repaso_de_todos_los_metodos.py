#Burbuja
def metodo_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j + 1]:
                numero_a_reemplazar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero_a_reemplazar
    return lista

print(metodo_burbuja([1,78,99,100,4,-5]))

