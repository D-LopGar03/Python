""" NUM_VALUES = 10

a = 0
print (a)
b = 1
print (b)

for _ in range (NUM_VALUES):
    r = a + b
    a = b
    b = r
    print (r) """

#Asigna un valor entero 2001 a la variable space_odyssey y muestra su valor

""" space_odyssey = 2001
print (space_odyssey) """

#Descubre el tipo del literal 	Good night & Good luck	

""" text = "Good night & Good luck"
print(type(text)) """

#Asigna la expresión 10 * 3.0 a la variable result y muestra su tipo.

result = 10 * 3.0

print (result)

print("Sucesión de fibonacci: ")

NUM_VALUES = int(input("¿Cuántos números contendrá esta sucesión?: "))

a = 0
print (a)
b = 1
print (b)

for _ in range (NUM_VALUES - 2):
    r = a + b
    a = b
    b = r
    print (r)