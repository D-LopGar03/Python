x = 0
f = 0
pares = 0
impares = 0

cantidad = int (input ("¿Cuántos números va a ingresar? "))

while x < cantidad:
    x = x+1
    n = int(input('Ingrese el valor: '))

    if n % 2==0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Hay ", pares, " pares y", impares, " impares")


while x < cantidad:
    x = x+1

    if n % 2==0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Hay ", pares, " pares y", impares, " impares")

for f in range (x<cantidad):


    if f%2==0:
        print("\n")
        print(f)
    else:
        print("feo")



