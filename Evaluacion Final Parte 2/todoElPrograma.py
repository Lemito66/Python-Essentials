from contrasena import contrasena
from diccionario import diccionario
from iteracionTipoDato import iteracionTipoDato
from paresEImpares import numerosParesEImpares
from tipoDatos import tipoDato
entrada = input(
    "Ingrese 1) Contraseña\n2)Diccionario\n3)IteracionTipoDato\4)Pares e Impares\n5)Tipo de Datos\n")
try:
    if int(entrada) == 1:
        print(contrasena())
    elif int(entrada) == 2:
        print(diccionario())
    elif int(entrada) == 3:
        print(iteracionTipoDato())
    elif int(entrada) == 4:
        print(numerosParesEImpares())
    elif int(entrada) == 5:
        print(tipoDato())
    else:
        print("Vuelva a intentarlo")
    
except(TypeError, ValueError,ZeroDivisionError,NameError,RuntimeError):
    print("Error")
