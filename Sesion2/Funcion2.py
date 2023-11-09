#Calculadora funciones

def FuncionResta():
    numero1 = float(input("Ingresa un numero: "))
    numero2 = float(input("Ingresa un segundo numero: "))
    resultadoResta = numero1 - numero2
    print("Resta: ", resultadoResta)
    
def funcionSuma():
    numero1 = float(input("Ingresa un numero: "))
    numero2 = float(input("Ingresa un segundo numero: "))
    resultadoSuma = numero1 + numero2
    print("Resta: ", resultadoSuma)
    
def menu():
    while True:
        print("Que operacion desea realizar: \n1)Suma \n2)Resta \n3)Salir")
        opcion = int(input("Opcion: "))
        if(opcion == 1 ):
            funcionSuma()
        elif(opcion == 2):
            FuncionResta()
        elif(opcion == 3):
            print("Hasta la proximaaaaa :(")
            break
        
menu()