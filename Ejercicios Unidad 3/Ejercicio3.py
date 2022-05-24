''' 3. Se necesita una aplicación que devuelva el menor de dos
números ingresados. '''
numeroUno = int(input("Ingrese el primer número: "))
numeroDos = int(input("Ingrese el primer número: "))
if numeroUno < numeroDos:
    print(f"El {numeroUno} es menor que {numeroDos}")
elif numeroDos < numeroUno:
    print(f"El {numeroDos} es menor que {numeroUno}")
else:
    print(f"El {numeroUno} es igual que {numeroDos}")


