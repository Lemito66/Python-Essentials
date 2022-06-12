""" Escriba un programa en el cual se pida ingresar tres números, comprueba que los tres números sean necesariamente diferentes y que saque el número intermedio de ellos. Si dos de ellos o los tres son iguales, se deberá escribir por consola que lo son.
Ejemplo:
Ingrese el primer número… 20
Ingrese el segundo número… 45
Ingrese el tercer número… 5

El número intermedio es 20.
"""
try: 
  primerNumero = int(input("Ingrese el primer numero: "))
  segundoNumero = int(input("Ingrese el segundo numero: "))
  tercerNumero = int(input("Ingrese el tercer numero: "))
  maximo = max(primerNumero, segundoNumero, tercerNumero)
  minimo = min(primerNumero, segundoNumero, tercerNumero)
  intermedio = (primerNumero+segundoNumero+tercerNumero)-minimo-maximo
  # print(intermedio)
  if primerNumero == segundoNumero and primerNumero == tercerNumero:
    print(f"Los numeros {primerNumero} , {segundoNumero}, {tercerNumero} son iguales")
  elif primerNumero == segundoNumero:
      print(f"Los numeros {primerNumero} , {segundoNumero} son iguales")
  elif primerNumero == tercerNumero:
      print(f"Los numeros {primerNumero} , {tercerNumero} son iguales")
  elif tercerNumero == segundoNumero:
      print(f"Los numeros {segundoNumero} , {tercerNumero} son iguales")
  else:
    print(f"El numero intermedio entre {primerNumero} , {segundoNumero}, {tercerNumero} es {intermedio}")
except (ValueError):
  print("Error")