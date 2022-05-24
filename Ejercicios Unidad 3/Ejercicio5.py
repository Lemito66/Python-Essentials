''' 5. Se necesita una aplicación que pueda calcular el área de un
triángulo o la de un círculo, que el usuario pueda elegir una de dos
opciones y dar el resultado en la pantalla. '''
entrada = int(input("Ingrese una opción\n1. Triangulo\n2.Circulo\n"))
if(entrada == 1):
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la base: altura: "))
    print(f"El área es: {(base*altura)/2}")
elif entrada == 2:
    radio = int(input("Ingrese el radio: "))
    print(f"El área es: {round(3.14159*radio**2)}")
else:
    print("Datos invalidos, vuelva a intentarlo")
