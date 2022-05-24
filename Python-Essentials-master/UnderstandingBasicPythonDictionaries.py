book = {'tittle': 'Sunrise News', 'author': 'Bob', 'year': 2010}
# print(book)
automovil = {'Chevrolet': 'Camaro', 'Color Auto': 'Plomo',
             'Tipo de Licencia': 'D', 'Millas por galon': '520', 'millas': '500'}
# print(book['author'])
# Saber la clave
''' for carro in automovil:
    print(carro) '''
print("color" + "=" + automovil['Color Auto'])
for key in automovil:  # Como saber clave con valor
    print(key + "= " + automovil[key])
