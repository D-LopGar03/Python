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

print("========================================")

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

print("========================================")

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

print("========================================")

longitud1 = len(sons1)

if sons1[0] == 0:
    print("Padre: ", parents1[0])
    print("Cantidad de hijos: ", sons1[0])
else:
    print("Padre: ", parents1[0])
    print("Cantidad de hijos: ", longitud1)

longitud2 = len(sons2)

if sons2[0] == 0:
    print("Padre: ", parents2[0])
    print("Cantidad de hijos: ", sons2[0])
else:
    print("Padre: ", parents2[0])
    print("Cantidad de hijos: ", longitud2)

longitud3 = len(sons3)

if sons3[0] == 0:
    print("Padre: ", parents3[0])
    print("Cantidad de hijos: ", sons3[0])
else:
    print("Padre: ", parents3[0])
    print("Cantidad de hijos: ", longitud3)

print("========================================")

for f in range(1):
    print("Padre: ", parents1[f])
    print("Madre: ", parents1[f + 1])
    for g in range(longitud1):
        if sons1[0] == 0:
            print("Esta familia no tiene hijos.") 
        else:
            print("Hijo: ", sons1[g])

print("========================================")

for f in range(1):
    print("Padre: ", parents2[f])
    print("Madre: ", parents2[f + 1])
    for g in range(longitud2):
        if sons2[0] == 0:
            print("Esta familia no tiene hijos.")        
        else:
            print("Hijo: ", sons2[g])

print("========================================")

for f in range(1):
    print("Padre: ", parents3[f])
    print("Madre: ", parents3[f + 1])
    for g in range(longitud3):
        if sons3[0] == 0:
            print("Esta familia no tiene hijos.") 
        else:
            print("Hijo: ", sons3[g])

print("========================================")