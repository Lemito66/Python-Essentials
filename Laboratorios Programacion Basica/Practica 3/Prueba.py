""" Escriba un programa que le solicite al usuario ingresar una 'm' si es masculino o una 'f' si es femenino. Seguídamente le pide la edad y finalmente le presenta un mensaje de saludo de acuerdo a la siguiente tabla de referencia del estado civil.
1. Soltero
2. Casado
3. viudo
4. unión libre
Si hay otros valores diferentes a los permitidos indicar mediante un mensaje que no se pudo procesar la información.

Ejemplo 1:
Ingrese su sexo. Masculino (m), Femenino (f)?... f
1. Soltero
2. Casado
3. viudo
4. unión libre
En base a la tabla anterior, ingrese el número de su estado civil?... 2
Buenos días, este programa ha determinado que usted está casada.
Gracias por usar este programa.

Ejemplo 2:
Ingrese su sexo. Masculino (m), Femenino (f)?... f
1. Soltero
2. Casado
3. viudo
4. unión libre
En base a la tabla anterior, ingrese el número de su estado civil?... 9
No se pudo procesar la información.
Gracias por usar este programa.  """

try: 
    entrada = input("Ingresar una 'm' si es masculino o una 'f' si es femenino: ")
    if entrada.lower() == 'm' or entrada.lower()=='f':
        edad = int(input("Ingresar una edad: "))
        tabla = int(input("1 Soltero\n2. Casado\n3.viudo\n4. unión libre\n"))
        if tabla == 1:
            print("Buenos días, este programa ha determinado que usted está Soltero")
        elif tabla == 2:
            print("Buenos días, este programa ha determinado que usted está Casado")
        elif tabla == 3:
            print("Buenos días, este programa ha determinado que usted está Viudo")
        elif tabla == 4:
            print("Buenos días, este programa ha determinado que usted está Union Libre")
        else:
            print("No se pudo procesar la información.\nGracias por usar este programa.")
    else:
        print("Intente de nuevo")
except(ValueError):
    print("No se pudo procesar la información.\nGracias por usar este programa.")

