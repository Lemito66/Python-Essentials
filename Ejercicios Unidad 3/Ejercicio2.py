''' 2. Se necesita una aplicación que pida una cantidad de segundos y
que devuelva cuántas horas, minutos y segundos son. '''
segundoIngresado = float(input("Ingrese la cantidad de segundos: "))
print(
    f"La cantidad en segundos: {segundoIngresado} \nen horas es {round(segundoIngresado/3600)} horas\nen minutos es {round(segundoIngresado/60)} minuto\nen segundos {segundoIngresado} segundos")
