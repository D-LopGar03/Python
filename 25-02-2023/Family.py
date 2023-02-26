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
    
    if answer == "n":
        valor = 0
        cantSons.append(valor)        
    elif answer == "s":
        sons.append(valor)
        valor=int(input("¿Cuántos hijos tienen?: "))
        cantSons.append(valor)
        for h in range(valor):
            print("Ingrese el nombre del hijo ", (h+1))
            hijo = str(input())
            sons.append(hijo)
  
            
cantidadHijos = len(cantSons)            
for j in range(0, 6, 2):
    print("Padre: ", parents[j], cantSons[j])
    
    


    