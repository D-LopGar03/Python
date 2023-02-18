x = 1
y = 1
sumaListaUno = 0
sumaListaDos = 0
promMa = 0
promTa = 0
SueldoMa=[]
SueldoTa=[]

print('Ingrese los sueldos de los trabajadores de la mañana: ')

while x != 0:
    x = x + 1
    n = float(input('Ingrese el sueldo de cada uno de ellos: '))
    SueldoMa.append(n)
    sumaListaUno = sumaListaUno + n
    x = n
    
Longitud1 = len(SueldoMa)
Longitud1 = Longitud1 -1

print('Sueldos de la mañana: ', SueldoMa, '= ', sumaListaUno)

print('Ingrese los sueldos de los trabajadores de la tarde: ')

while y != 0:
    y = y + 1
    n = float(input('Ingrese el sueldo de cada uno de ellos: '))
    SueldoTa.append(n)
    sumaListaDos = sumaListaDos + n
    y = n
    
Longitud2 = len(SueldoTa)
Longitud2 = Longitud2 - 1

print('Sueldos de la tarde: ', SueldoTa, '= ', sumaListaDos)

promMa = sumaListaUno/Longitud1
print('El promedio de sueldos de la mañana es de', promMa)
promTa = sumaListaDos/Longitud2
print('El promedio de sueldos de la tarde es de', promTa)


if sumaListaUno>sumaListaDos:
    print('Los sueldos de la mañana son mayores que los de la tarde')

else:
    print('Los sueldos de la tarde son mayores que los de la mañana')


