# Las f-strings son una característica introducida en Python 3.6 
# que proporciona una forma concisa y legible de formatear cadenas de texto. 
# Las f-strings te permiten incluir expresiones dentro de las cadenas, que son evaluadas
# y luego formateadas en el resultado final.


# Ejemplo 1

animal = "hormiga"
name = "Carlos"
high = 0.2

print(f"\nHola, me llamo {animal} soy un {name} y mido {high} metros")

# Son válidas la operaciones dentro de estas, ya que son evaluadas antes de ejecutarlas, pero los valores a operar siempre deben de ir dentro un
# juego de llaves

# Ejemplo 2

print(f"\n((5+8)*8)={(5+8)*8}")

# Ejemplo 3

name = str(input("\nIngresa tu nombre: "))
age = int(input("Ingresa tu edad: "))
fruit = str(input("Ingresa tu fruta favorita: "))
fruit = fruit.lower()
num_uno = int(input("Ingresa un número: "))
num_dos = int(input("Ingresa un número: "))

if fruit.endswith("a"):
    print(f"Hola {name}, sé que tienes {age} años, tu fruta favorita es la {fruit} y la multiplicación de {num_uno} * {num_dos} es {num_uno * num_dos}.")
elif fruit.endswith("n"):
    print(f"Hola {name}, sé que tienes {age} años y tu fruta favorita es el {fruit} y la división de {num_uno} / {num_dos} es {num_uno / num_dos}.")