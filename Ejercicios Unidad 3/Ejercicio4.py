''' 4. Se necesita una aplicación que clasifique a las personas según
sus rangos de edad en diferentes grupos. '''
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 3:
    print("Usted es un bebe")
elif edad >= 4 and edad <= 12:
    print("Usted es un niño")
elif edad >= 12 and edad <= 17:
    print("Usted es adolescente")
elif edad >= 18 and edad <= 64:
    print("Usted es mayor de edad")
elif edad >= 65 and edad <= 200:
    print("Usted es de la tercera edad")
else:
    print("Edad invalida!")
