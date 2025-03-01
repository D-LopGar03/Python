def bienvenida():
    print("===============================================")
    print("Hola, este programa convertirá números a letras")
    print("===============================================")
    num = int(input("Ingresa un número: "))
    convertir(num)

def convertir(num):
    if num == 0:
        print("Cero")
    elif num == 1:
        print("Uno")
    elif num == 2:
        print("Dos")
    elif num == 3:
        print("Tres")
    else:
        print("Este programa imprime los números del cero al tres")

bienvenida()
