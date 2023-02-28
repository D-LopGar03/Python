"""  # Resolver ((3+2)/(2*5))**2

suma = 3 + 2
multipli = 2*5
division = suma / multipli
cuadrado = division ** 2
print(cuadrado)

print(((3+2)/(2*5))**2)

# Resolver pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde

name = str(input("¿Cómo se llama el empleado?: "))
nam1 = name.title
print("¿Cuántas horas ha trabajado ",nam1, "?: ")
horas = int(input())

print(name.title, " merece por haber trabajado ", horas, (horas * 33000), " pesos")

#Calcular IMC 

peso = float(input("¿Cuánto pesas?: "))
altura = float(input("¿Cuánto mides?: "))
imc = round(float(peso)/float(altura)**2,2)
print("Tu índice de masa corporal es", imc) 

# Mostrar cociente y residuo

n = float(input("Ingrese un número cualquiera: "))
m = float(input("Ingrese un número cualquiera: "))

print("El cociente es: ", (n/m))
print("El residuo es: ", (n%m)) 

invertir = float(input("¿Cuánto dinero desea invertir?: "))
years = int(input("¿A cuántos años desea hacer la inversión?: "))
interes = float(14.5/100)

rendimiento = round(((invertir*interes)/100)*years, 2)

print("El rendimiento de la cantidad invertida a ", years, " años es de $", rendimiento)"""

# Calcular el peso total de una entrega de payasos y muñecas, los payasos pesan 112g y las muñecas 75g

PesoPayaso = 0.112
PesoMuneca = 0.075

CantPay = int(input("¿Cuántos payasos se van a enviar?: "))
CanMun = int(input("¿Cuántas muñecas se van a enviar?: "))

Total = ((CantPay*PesoPayaso)+(CanMun*PesoMuneca))

print("El peso total de la entrega es de ", Total, "kg")

