import pandas as pd
x = 0
y = 0
SumaÑana = 0
SumaTarde = 0
NombreMañana = []
SueldoMañana = []
NombreTarde = []
SueldoTarde = []

print('Ingrese los nombres y sueldos de la mañana')

while x <= 4:
    n = str(input("Ingrese el nombre del trabajador: "))
    NombreMañana.append(n)
    s = float(input("Ingrese el sueldo: "))
    SueldoMañana.append(s)
    SumaÑana = SumaÑana + s
    x = x + 1


print(NombreMañana)
print(SueldoMañana)

print('Ingrese los nombres y sueldos de la tarde')

while y <=4:
    n = str(input("Ingrese el nombre del trabajador: "))
    NombreTarde.append(n)
    s = float(input("Ingrese el sueldo: "))
    SueldoTarde.append(s)
    SumaTarde = SumaTarde + s
    y = y + 1
    
print(NombreTarde)
print(SueldoTarde)


print("Los sueldos de la mañana suman: ", SumaÑana)
print("Los sueldos de la tarde suman: ", SumaTarde)

if SueldoMañana > SueldoTarde:
    print("Los trabajadores de la mañana suponen un gasto mayor que los de tarde")
else:
        print("Los trabajadores de la tarde suponen un gasto mayor que los de mañana")
