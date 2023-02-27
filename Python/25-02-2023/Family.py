parents1 = []
parents2 = []
parents3 = []
sons1 = []
sons2 = []
sons3 = []
a = 0


for f in range (1):
    father = str(input("Ingrese el nombre del padre: "))
    mother = str(input("Ingrese el nombre de la madre: "))
    parents1.append(father)
    parents1.append(mother)
    answer = str(input("¿Tienen hijos? s/n: "))
    if answer == "s" or answer == "S":
        cant = int(input("¿Cuántos hijos tienen?: "))
        for cantidad in range(cant):
            print("Ingrese el nombre del hijo ", (cantidad + 1))
            hijo = str(input(""))
            sons1.append(hijo)
    elif answer == "n" or answer == "N":
        valor = 0
        sons1.append(valor)  

for f in range (1):
    father = str(input("Ingrese el nombre del padre: "))
    mother = str(input("Ingrese el nombre de la madre: "))
    parents2.append(father)
    parents2.append(mother)
    answer = str(input("¿Tienen hijos? s/n: "))
    if answer == "s" or answer == "S":
        cant = int(input("¿Cuántos hijos tienen?: "))
        for cantidad in range(cant):
            print("Ingrese el nombre del hijo ", (cantidad + 1))
            hijo = str(input(""))
            sons2.append(hijo)
    elif answer == "n" or answer == "N":
        valor = 0
        sons2.append(valor) 

for f in range (1):
    father = str(input("Ingrese el nombre del padre: "))
    mother = str(input("Ingrese el nombre de la madre: "))
    parents3.append(father)
    parents3.append(mother)
    answer = str(input("¿Tienen hijos? s/n: "))
    if answer == "s" or answer == "S":
        cant = int(input("¿Cuántos hijos tienen?: "))
        for cantidad in range(cant):
            print("Ingrese el nombre del hijo ", (cantidad + 1))
            hijo = str(input(""))
            sons3.append(hijo)
    elif answer == "n" or answer == "N":
        valor = 0
        sons3.append(valor) 

longitud1 = len(sons1)
print("Padre: ", parents1[0])
print("Cantidad de hijos: ", longitud1)

longitud2 = len(sons2)
print("Padre: ", parents2[0])
print("Cantidad de hijos: ", longitud2)

longitud3 = len(sons2)
print("Padre: ", parents3[0])
print("Cantidad de hijos: ", longitud3)

for f in range(1):
    print("Padre: ", parents1[f])
    print("Madre: ", parents1[f + 1])
    for g in range(longitud1):
        print("Hijo: ", sons1[g])

for f in range(1):
    print("Padre: ", parents2[f])
    print("Madre: ", parents2[f + 1])
    for g in range(longitud2):
        print("Hijo: ", sons2[g])

for f in range(1):
    print("Padre: ", parents3[f])
    print("Madre: ", parents3[f + 1])
    for g in range(longitud3):
        print("Hijo: ", sons2[g])