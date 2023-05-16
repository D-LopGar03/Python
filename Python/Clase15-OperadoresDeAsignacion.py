""""
Un operador de asignación es un tipo de operador utilizado en programación para asignar un valor a una variable. El operador de asignación se utiliza para actualizar o modificar el valor de una variable existente en un programa.

En la mayoría de los lenguajes de programación, el operador de asignación se representa mediante el símbolo "=" (igual). Cuando se utiliza este operador, el valor a la derecha del símbolo "=" se asigna a la variable a la izquierda.

Por ejemplo, si tenemos una variable "x" y queremos asignarle el valor 5, podemos utilizar el operador de asignación de esta manera:

x = 5

Este código asigna el valor 5 a la variable "x". En algunos lenguajes de programación, como Python, también se pueden utilizar operadores de asignación compuesta, como "+=", "-=", "*=", "/=" y "%=", que combinan una operación aritmética con la asignación.

Por ejemplo, la expresión "x += 5" es equivalente a "x = x + 5", que aumenta el valor de la variable "x" en 5.

"""

""" x = 589  # asignamos el valor inicial de 589 a la variable x

x += 10  # x = x + 10 (Le sumamos 10 a la variable x y el resultante es el valor inicial aumentado en 10)
print(x) # 599



x -= 20  # x = x - 20 (Le restamos 20 a la variable x y el resultante es el valor inicial decrementado en 20)
print(x) # 579



x *= 2   # x = x * 2 (Le multiplicamos 2 a la variable x y el resultante es el valor inicial multiplicado en 2)
print(x) # 1178



x /= 3   # x = x / 3 (Le dividimos 3 a la variable x y el resultante es el valor inicial divido en 3)
print(x) # 386.0



x %= 7   # x = x % 7 (Muestra el restante de dividir entre 7)     
print(x) # 4.0



x //= 7   # x = x % 7 (Muestra la división entera de x entre 7)     
print(x) # 0.0

x **= 8 # x = x ** 8 (Muestra la potencia de x a la 8)
 """

x = 1

nombre = "Hola "
nombre += input("Escribe tu nombre: ")

print(nombre,"este es el incremento y decremento de una variable")

print("\nIncremento\nEl valor inicial de x es: ",x)
x += 15
print("El valor final de x es: ",x)

print("\nDecremento\nEl valor inicial de x es: ",x)
x -= 32
print("El valor final de x es: ",x,"\n")

