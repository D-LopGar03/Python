employee=[]
salary=[]
sumaSueldo = 0

for i in range(0, 3):
    print("Ingrese el nombre del empleado ", (i+1), ": ")
    e = input()
    employee.append(e)
    
    for j in range(0, 3):
        print("Ingrese el sueldo para el mes", (j+1), ": ")
        s = int(input())    
        
        sumaSueldo = sumaSueldo + s
    salary.append(sumaSueldo)
    sumaSueldo = 0
    

for f in range(3):
    print(employee[f], salary[f])

mayor=salary[0]
nombre=employee[0]

for x in range(1,3):
    if salary[x] > mayor:
        mayor = salary[x]
        nombre = employee[x]
print("La persona con el mayor gasto salarial fue", nombre, " con un total de $", mayor)

