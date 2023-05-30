# Otra manera de concatenar texto con números sin convertir los números a texto antes o sin llevar comas

name = "Carlos"
animal = "hormiga"
age = 555

# Opción 1

print("Hola {} eres un {} y tienes {} años.".format(animal, name, age))

# Opción 2

print("Hola {name} eres un {ser} y tienes {age} años.".format(ser="motherfoca", name="Pepe", age=30))

# Opción 3, esta a diferencia de las anteriores, no le importa el orden en como vayan las variables dentro del método format,
# ya que se identifican por números según el orden en el que se declaren y dentro de las llaves se puede llamar cualquier número

print("Hola {2} eres un {1} y tienes {0} años.".format(animal, name, age))
