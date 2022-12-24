#Metodo Burbuja


def metodo_burbuja(lista):
    '''
    Revisa cada elemento de la lista con el siguiente elemento,         
    intercambiandolo de posición si estan en el orden equivocado
    '''
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j + 1]:
                guardar_numero_para_ser_reemplazado = lista[j]
                lista[j] = lista [j + 1 ]
                lista[j + 1] = guardar_numero_para_ser_reemplazado
                
    return lista
 
print(metodo_burbuja([2,8,7,6,3,2,1,20,19,0]))