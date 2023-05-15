print("\n***************************************************\n* Programa que determina qué número es más grande *\n***************************************************\n")

def inicio():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    comparar(num1, num2, num3)

def comparar(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        print(num1, "es el mayor de los tres.")
    else:
        if num2 > num3:
            print(num2, "es el mayor de los tres")
        else:
            print(num3, "es el mayor de los tres")   
    if num1 == num2 and num1 == num3:
        print("Los tres números son iguales.")

inicio()