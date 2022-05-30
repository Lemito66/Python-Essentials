def contrasena():
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

