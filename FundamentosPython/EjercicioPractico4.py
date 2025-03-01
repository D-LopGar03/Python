import time

def inicio():
    print("Calculadora con una sola variable\n")
    print("********************\n* Menú de opciones *\n********************\n")
    print("1) Suma\n2) Resta\n3) Multiplicación\n4) División\n5) División entera\n6) Exponente\n7) Módulo o resto\n")
    choice = int(input("Ingresa tu opción: "))
    if choice == 1:
        suma()
    elif choice == 2:
        resta()
    elif choice == 3:
        multiplicacion()
    elif choice == 4:
        division()
    elif choice == 5:
        divEnt()
    elif choice == 6:
        exponent()
    elif choice == 7:
        mod()
    else:
        print("Opción inválida...\n")
        time.sleep(1)
        inicio()
           
def suma():
    print("Elegiste suma")
    x = float(input("Ingresa el primer número: "))
    x += float(input("Ingresa el segundo número: "))
    print("El resultado de la suma es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def resta():
    print("Elegiste resta")
    x = float(input("Ingresa el primer número: "))
    x -= float(input("Ingresa el segundo número: "))
    print("El resultado de la resta es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def multiplicacion():
    print("Elegiste multiplicación")
    x = float(input("Ingresa el primer número: "))
    x *= float(input("Ingresa el segundo número: "))
    print("El resultado de la multiplicación es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def division():
    print("Elegiste división")
    x = float(input("Ingresa el primer número: "))
    x /= float(input("Ingresa el segundo número: "))

    print("El resultado de la división es: ",round(x,2))

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def divEnt():
    print("Elegiste división entera")
    x = float(input("Ingresa el primer número: "))
    x //= float(input("Ingresa el segundo número: "))
    print("El resultado de la división entera es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def exponent():
    print("Elegiste exponente")
    x = float(input("Ingresa el primer número: "))
    x **= float(input("Ingresa el segundo número: "))
    print("El resultado del exponente es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()

def mod():
    print("Elegiste módulo o residuo")
    x = float(input("Ingresa el primer número: "))
    x %= float(input("Ingresa el segundo número: "))
    print("El resultado del residuo es: ",x)

    opc = str(input("¿Reiniciar? s/n: "))
    opc = opc.lower()

    if opc == "s":
        inicio()
    else:
        exit()
     
inicio()