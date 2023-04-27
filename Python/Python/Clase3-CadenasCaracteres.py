#Manipulación de strings

#La asignación consiste en asignar una cadena de caracteres a otra, para lo cual es necesario utilizar el operador +=

print("Esto es asignación")
mensaje = "Hola"
mensaje += " "
mensaje += "Damian"

print(mensaje)

#La concatenación es una operación que consiste en unir dos cadena o más, para formar una cadena de mayor tamaño, para lo cual es nesecario utilizar el signo +

print("Esto es concatenación")
mensaje = "Hola"
espacio = " "
nombre = "Damian"
print(mensaje + espacio + nombre)

#Concatenando números y letras

numeroUno = 4
numeroDos = 6

resultado = numeroUno + numeroDos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

#La búsqueda consiste en localizar  dentro de una cadena una subcadena más pequeña a un carácter por lo cuál es necesario utilizar el método find
print("Búsqueda")

mensaje = "Hola Damian"
buscar_subcadena = mensaje.find("Damian")
print(buscar_subcadena)

#La extracción consiste en sacar fuera de una cadena, una porción de la misma según su posición dentro de ella, para ello es nesecario indicar la posición a extraer [1:8]

mensaje = "Hola Damian"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

#La comparación se utiliza para comparar dos cadenas de caracteres, para ello se utiliza el operador ==
print("Comparación")

mensaje_Uno = "Hola"
mensaje_Dos = "Adiós"
#Imprime verdadero si ambas cadenas son iguales, de lo contrario sería falso
print(mensaje_Uno == mensaje_Dos)