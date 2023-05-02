def introducing():
    print("\nIngresa dos números a comparar...\n")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print("\nLos números a comparar son", num1, "y", num2, "\n")
    comparation(num1, num2)

def comparation(num1, num2):
    if num1 == num2: 
        print(num1, " == ", num2)
    if num1 >= num2: 
        print(num1, " >= ", num2)
    if num1 <= num2: 
        print(num1, " <= ", num2)
    if num1 < num2: 
        print(num1, " < ", num2)
    if num1 > num2: 
        print(num1,  " > ", num2)
    if num1 != num2: 
        print(num1, " != ", num2)
    print("\n")

introducing()