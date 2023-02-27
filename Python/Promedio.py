#Cargar dos listas de números de 10 valores las dos que me sume los valores por separados de ambas listas y 
#me diga que lista es mayor en la sumatoria

x = 1
y = 1
sumaListaUno = 0
sumaListaDos = 0

cantidad = 10
cantidadDos = 10

print('Ingrese los datos de la lista uno')

while x <= cantidad:
    x = x+1
    n = int(input('Ingrese el valor: '))
    sumaListaUno = sumaListaUno + n

print('Ingrese los datos de la lista dos')

while y <= cantidadDos:
    y = y+1
    n = int(input('Ingrese el valor: '))
    sumaListaDos = sumaListaDos + n

if sumaListaUno>sumaListaDos:
    print('La lista uno es mayor')
else:
    print('La lista dos es mayor') 