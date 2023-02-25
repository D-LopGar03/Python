print("\t\tTaller D-Low")

detalles=['Coche', 'Modelo', 'Precio']
marca=[]
modelo=[]
precio=[]
for x in range(3):
    mar=input("Ingrese la marca del coche: ")
    marca.append(mar)
    mod=input("Ingrese el modelo: ")
    modelo.append(mod)
    price=int(input("Ingrese el precio del coche: $"))
    precio.append(price)
    
    
print(detalles)

for x in range(0):
    print(detalles[x])
    
for x in range(3):
    print(marca[x], modelo[x], precio[x])
    
for x in range(2):
    if precio[x]>precio[x+1]:
        aux=precio[x]
        precio[x]=precio[x+1]
        precio[x+1]=aux
        
print("El coche más caro vale: ", x)
        