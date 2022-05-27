'''Desarrollar un programa que permita validar la contraseña introducida por un usuario con las
siguientes comprobaciones:
 Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
 Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
 Debe contener al menos un número entre 0 y 9.
 Debe contener un símbolo especial entre: $,%,*,@
 Tamaño mínimo de 5 caracteres y máximo de 15. Listo
Se debe solicitar la contraseña al usuario, así como informarle sobre estos requisitos para su
contraseña, una vez validada mostrar un mensaje al usuario informándole al respecto.
'''
#any([True if i in letraMinuscula else False for i in password])
password = input("Ingrese su contraseña: ")
letraMinuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letraMayuscula = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
simboloEspecial = ['$', '%', '*', '@']
numero = [1, 2, 3, 4, 5, 6, 7, 8]
if len(password) <= 5 or len(password) >= 15:
    print("Su longitud debe tener un mínimo de 5 caracteres y máximo de 15.")
elif not any(i in letraMinuscula for i in password):
    print("Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
elif not any(i in letraMayuscula for i in password):
    print("Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
elif not any(i in simboloEspecial for i in password):
    print("Debe contener un símbolo especial entre $', '%', '*', '@")
elif not any(i in str(numero) for i in password):
    print("Debe contener al menos un número entre 0 y 9.")
else:
    print("Contraseña ingresada exitosamente")
        

# nombre = "Emill"
# lista=['e','l']
# for i in nombre.lower():
#     if i in lista:
#         print(i)
