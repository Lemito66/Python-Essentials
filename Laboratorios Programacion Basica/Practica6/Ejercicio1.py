'''Escriba un programa que pida un símbolo o frase al usuario, y cuántas veces se ha de repetir y que lo mueva a través de la pantalla en diagonal con un salto que indique el usuario también. Tomar en cuenta las dimensiones de la pantalla en C# (25 x 80). En el caso de superar los rangos de pantalla, se regresará.
Ejemplo:
Ingrese símbolo o frase… **
Salto… 8
Numero de repeticiones: 12
**
        **
                **
                        **
                                **
                                        **
                                                **
                                                        **
                                                                **
                                                                        **
                                                                              **
                                                                      **


'''
""" for i in range(1, 10, 2):
    print(("*"*i).center(10)) """
simbolo_O_Frase=input("Ingrese simbolo o frase: ")
salto=int(input("Cuantos saltos: "))
saltoCopia=salto
espacio=0
cuantasVecesSeRepite=int(input("Cuantas veces se repite: "))
for i in range(1, cuantasVecesSeRepite+1):
    # if salto>80:       
    #     espacio -= salto * cuantasVecesSeRepite;
    #     cuantasVecesSeRepite += 2;      
    print(simbolo_O_Frase,end="" +"\n"+" "*salto)
    salto+=saltoCopia
    

