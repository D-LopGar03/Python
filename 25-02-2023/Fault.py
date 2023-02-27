trabajador1 = []
trabajador2 = []
trabajador3 = []
diaTr1 = []
diaTr2 = []
diaTr3 = []
diaFalt1 = []
diaFalt2 = []
diaFalt3 = []

for a in range(1):
    name = str(input("Ingrese el nombre del empleado: "))
    trabajador1.append(name)
    diaF = int(input("¿Cuántos día faltó?: "))
    diaTr1.append(diaF)
    for b in range(diaF):
        diaFaltado = int(input("Ingrese el día del mes en qué faltó: "))
        diaFalt1.append(diaFaltado)

for a in range(1):
    name = str(input("Ingrese el nombre del empleado: "))
    trabajador2.append(name)
    diaF = int(input("¿Cuántos día faltó?: "))
    diaTr2.append(diaF)
    for b in range(diaF):
        diaFaltado = int(input("Ingrese el día del mes en qué faltó: "))
        diaFalt2.append(diaFaltado)

for a in range(1):
    name = str(input("Ingrese el nombre del empleado: "))
    trabajador3.append(name)
    diaF = int(input("¿Cuántos día faltó?: "))
    diaTr3.append(diaF)
    
    for b in range(diaF):
        diaFaltado = int(input("Ingrese el día del mes en qué faltó: "))
        diaFalt3.append(diaFaltado)

longitud1 = len(diaFalt1)
longitud2 = len(diaFalt2)
longitud3 = len(diaFalt3)

for a in range(1):   
    print(trabajador1[a])

for a in range(longitud1):    
    print(diaFalt1[a])

for a in range(1):   
    print(trabajador2[a])

for a in range(longitud2):
    print(diaFalt2[a])

for a in range(1):   
    print(trabajador3[a])

for a in range(longitud3):
    print(diaFalt3[a])

if longitud1 > longitud2 and longitud1 > longitud3:
    for a in range (1):
        print("El trabajador qué más días faltó fue: ", trabajador1[a], "(", longitud1,") días")
elif longitud2 > longitud1 and longitud2 > longitud3:
    for a in range (1):
        print("El trabajador qué más días faltó fue: ", trabajador2[a],"(", longitud2,") días")
else:
    for a in range (1):
        print("El trabajador qué más días faltó fue: ", trabajador3[a],"(", longitud3,") días")
    
