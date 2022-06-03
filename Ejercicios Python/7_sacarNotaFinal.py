def notaFinal():
    try:
        notaUno = float(input("Ingresa la primera nota: "))
        notaDos = float(input("Ingresa la segunda nota: "))
        notaTres = float(input("Ingresa la tercera nota: "))
        notaFinal=(notaUno)+(notaDos)+(notaTres)/3
        if notaFinal >=7:
            return "Buena nota"
        else:
            return "Perdiste el año"      
        #return notaFinal
    except(TypeError,ValueError):
        return "Error"
print(notaFinal())
