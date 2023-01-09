#Burbuja
def metodo_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j + 1]:
                numero_a_reemplazar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero_a_reemplazar
    return lista

def metodo_por_seleccion_ascendente(lista):
    for i in range(len(lista)):
        numero_minimo = i
        for j in range(numero_minimo + 1, len(lista)):
            if lista[j] < lista[numero_minimo]:
                numero_minimo = j
        numero_a_reemplazar = lista[i]
        lista[i] = lista[numero_minimo]
        lista[numero_minimo] = numero_a_reemplazar
    return lista

print(metodo_burbuja([1,78,99,100,4,-5]))
print(metodo_por_seleccion_ascendente([1,78,99,100,4,-5]))