def edadActual(year):
    year = input("Ingrese el año de su nacimiento")
    fechaActual=2022
    try:
        yearsActually=fechaActual-int(year)
        print(f'Usted tiene {yearsActually} años')
    except(TypeError,ValueError):
        print("Error")
    
print(edadActual(1998))
        