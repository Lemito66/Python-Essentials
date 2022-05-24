import random
diccionary = {'Nombre': 'Emill', 'Apellido': 'Logroño', 'Cedula': 1}
book = {'tittle': 'Sunrise News', 'author': 'Bob', 'year': 2010}
account = random.randrange(1, 100)
print(account)
''' for i in range(1,account):
    print(i) '''


def visualizarDiccionario(diccionary):
    for key in diccionary:
        print(key + "=" + str(diccionary[key]))


visualizarDiccionario(book)
