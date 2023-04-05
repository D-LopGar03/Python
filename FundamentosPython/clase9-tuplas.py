number = (1, 2, 3, 4, 5, 6) #Tupla
lista = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 2, 2] #Lista

print (type(number))
print (number[2])
lista[2] = "Hola Mundirijillo"
print(lista)

#Saber la posición de un elemento

print(number.index(2))

#Saber si un cuántos elementos están repetidos en la lista

print(lista.count(2))

if lista.count(2) == 3:
    print("Puto")

#Convertir una lista en una tupla y una tupla en una lista
print(list(number))
print(tuple(lista))