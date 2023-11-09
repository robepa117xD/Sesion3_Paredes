#un estructura de control selectiva if aninado es el conjunto de
#de diversos if y diversas condiciones 
#realizar un menu para inventarios
#Una estructra de control ciclica, repetitiva , iterativa, genera bucles o repeticiones
#La estructura de control while evalua una condicion y si es verdadera se detiene programa

while True:
    print("Menu inventarios \n1)Ingresar articulo \n2)Consulta \n3)Salir")
    opcion = int(input("Que opcion desea realizar: "))

    if (opcion == 1):
        print("Modulo de alta Articulos :D")
    elif (opcion == 2):
        print("Modulo de consulta Articulos")
    elif (opcion == 3):
        print("Finalizo el programa")
        break