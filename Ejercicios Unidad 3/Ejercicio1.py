''' 1. Se necesita una aplicación que verifique si una frase es un
palíndromo. '''
cadena=input("Ingresa una frase: ")
#cadenaNueva=cadena.replace(" ","")[::-1].lower()
#cadenaNueva=cadena[::-1]
# print(cadena.replace(" ","").lower())
# print(cadenaNueva)
if cadena.replace(" ","").lower()== cadena.replace(" ","")[::-1].lower(): #print("3".join(cadenaOcho)) cadena[::-1]
    print("Es palindromo")
else:
    print("No es palindroma")