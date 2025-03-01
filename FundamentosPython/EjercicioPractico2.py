print("\n******************************************************\n* Programa que determina si un numero es par o impar *\n******************************************************")

def inicio():
    num = float(input("\nIngresa un número para identificar si es par o impar: "))
    print(num % 2)
    comparar(num)

def comparar(num):
    if num % 2==0:
        print(num," es par")
    else:
        print(num, "es impar")

inicio()