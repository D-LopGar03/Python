parents = []
sons = []
cantSons = []
valor = 0
x = 0

for i in range(3):
    father = input("Nombre del padre: ")
    mother = input("Nombre de la madre: ")
    parents.append(father)
    parents.append(mother)
    answer = input("¿Tienen hijos? s/n: ")
    
    if answer == "s" or answer == "S":
        sons.append(valor)
        valor=int(input("¿Cuántos hijos tienen?: "))
        cantSons.append(valor)
        for h in range(valor):
            print("Ingrese el nombre del hijo ", (h+1))
            hijo = str(input())
            sons.append(hijo)
    elif answer == "n" or answer == "N":
        valor = 0
        cantSons.append(valor)      
               
print("Listado del padre y la cantidad de hijos qué tiene: ")            
""" cantidadHijos = len(cantSons)    """         
for j in range(0, 6, 2):
    print("Padre: ", parents[j])
    if j == 0:
        for x in range(1):
            print("Cantidad de hijos: ",cantSons[0])
    elif j == 2:
        for x in range(1):
            print("Cantidad de hijos: ",cantSons[1])
    elif j == 4:
        for x in range(1):
            print("Cantidad de hijos: ",cantSons[2])
    
print("Listado del padre, madre e hijos: ")  
cantidadHijos = len(cantSons) 
for padres in range(1,7):

    print("Padre: ", parents[0])
    print("Madre: ", parents[1])
    
    for hijos in range(cantidadHijos):
        print("Hijo: ", sons[hijos])
