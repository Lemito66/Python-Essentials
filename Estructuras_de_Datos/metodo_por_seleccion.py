'''
Es un algoritmo que consiste en ordenar los elementos de manera ascendente o descendente
Funcionamiento
-Buscar el dato más pequeño de la lista
-Intercambiarlo por el actual
-Seguir buscando el dato más pequeño de la lista
-Intercambiarlo por el actual
-Esto se repetirá sucesivamente
'''


def metodo_por_seleccion_ascendente(lista):
    for i in range(len(lista)):
        numero_minimo = i
        for j in range(numero_minimo + 1, len(lista)):
            if lista[j] < lista[numero_minimo]:
                numero_minimo = j
        numero_para_ser_reemplazado = lista[i]
        lista[i] = lista[numero_minimo]
        lista[numero_minimo] = numero_para_ser_reemplazado
    return lista

print(metodo_por_seleccion_ascendente([4,2,6,8,5,7,0]))

def metodo_por_seleccion_descendente(lista):
    for i in range(len(lista)):
        numero_maximo = i
        for j in range(numero_maximo+1, len(lista)):
            if lista[j] > lista[numero_maximo]:
                numero_maximo = j
        numero_para_ser_reemplazado = lista[i]
        lista[i] = lista[numero_maximo]
        lista[numero_maximo] = numero_para_ser_reemplazado
    return lista

print(metodo_por_seleccion_descendente([4,2,6,8,5,7,0]))

