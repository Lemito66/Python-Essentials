""" Escriba un programa que pida la altura de una persona en metros y su peso en kilogramos. A continuación, se saca el IMC (Índice de Masa Corporal) y comprueba en qué categoría esta. En el caso de que tenga sobre peso, en qué tipo de sobre peso se encuentra; si tiene obesidad, qué tipo de obesidad tiene. Los rangos se basarán en la siguiente tabla: 
Ejemplo:
Ingrese su peso… 80,3
Ingrese su altura…1,70
Su IMC es de 27,79 y está en la categoría de Sobrepeso, de tipo II.
"""
try:
    altura=float(input("Ingrese su altura en metros"))
    peso=float(input("Ingrese su pero en kilogramos"))
    imc=peso/altura**2
    if altura >0 and peso >0:        
        if imc >=0 and imc <18.5:
            print(f"Su imc es {imc} y esta en Peso Insufiente")
        elif imc >= 18.5 and imc <25:
            print(f"Su imc es {imc} y esta en peso normal")
        elif imc >= 25 and imc <27:
            print(f"Su imc es {imc} y esta en Sobrepeso Tipo I")
        elif imc >= 27 and imc <30:
            print(f"Su imc es {imc} y esta en Sobrepeso Tipo II")
        elif imc >= 30 and imc <35:
            print(f"Su imc es {imc} y esta en Obesidad Tipo I")
        elif imc >= 35 and imc <40:
            print(f"Su imc es {imc} y esta en Obesidad Tipo II")
        elif imc >= 40 and imc <50:
            print(f"Su imc es {imc} y esta en Obesidad Tipo III")
        elif imc >= 50:
            print(f"Su imc es {imc} y esta en Obesidad Tipo Iv")
    else:
        print("Ingreso numeros negativos")
except(ValueError):
    print("Hubo un error")