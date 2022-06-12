""" Escriba un programa como un sistema de facturación, donde se genere un nuevo producto hasta que el usuario diga que ya no hay más productos. Para cada uno de los productos se pide un nombre (de máximo 6 letras), precio y cantidad comprados. Al final se imprime la factura (después de limpiar la pantalla), el subtotal, el IVA (12%), el total, pide el pago del cliente y se imprime el vuelto que se debe dar. El ejercicio debe ser a prueba de usuarios, en la medida de lo que se ha aprendido.
Ejemplo:
Producto #1
	Nombre: Leche
	Precio: 0,90
	Cantidad: 6
Desea ingresar un nuevo producto (S/N) … S
Producto #2
	Nombre: Agua
	Precio: 0,40
	Cantidad: 12
"""
import os
contadorProducto=0
subTotal=0
nombreProducto=[]
precioProducto=[]
cantidadCompradoProducto=[]
sumatoriaTodaLaLista=[]
while True:
    try:
        contadorProducto+=1
        print(f"Producto {contadorProducto}")
        nombreProducto.append(input("Ingrese un nombre de su producto: "))
        if len(nombreProducto) >= 0 and len(nombreProducto)<=6:
            precioProducto.append(float(input("Ingrese el precio del: ")))
            cantidadCompradoProducto.append(float(input("Ingrese la cantidad de su producto: ")))
            #print(f"Nombre: {nombreProducto}\nPrecio: ${precioProducto}\nCantidad: {cantidadCompradoProducto}")
            confirmacionn=input("Desea Ingresar un nuevo Producto (S/N):")
            if confirmacionn.upper()=='N':
                break
            elif confirmacionn.upper()=='S':
                continue
            else:
                print("Solo debe presionar N o S")
                break
        else:
            print("La longitud debe teneer un maximo de 6 letras")
            break
    except(ValueError,IndexError):
        print("Error")
        break

try:
    os.system('cls')
    print("NOMBRE          PRECIO   CANTIDAD  TOTAL")
    for i in range(len(nombreProducto)):
        total=cantidadCompradoProducto[i]*precioProducto[i]
        print("{0:10}{1:10}{2:10}{3:10}".format(nombreProducto[i],precioProducto[i],cantidadCompradoProducto[i],total))
        subTotal+=total
    print("Subtotal:","%.2f" % subTotal ,"USD")
    iva= (12*subTotal)/100
    print("IVA 12%:","%.2f" % iva,"USD")
    totalFactura=subTotal+iva
    print("TOTAL:","%.2f" % totalFactura,"USD")
    pagoCliente=float((input("Ingrese el pago del cliente: ")))
    cambio=pagoCliente-totalFactura
    print("Vuelto:","%.2f" % cambio,"USD")
except(ValueError,IndexError):
    print("Error")

