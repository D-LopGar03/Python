animal = "  chanchITo feliz  "
#Acá se está tomando todo en mayúsculas
print(animal.upper())
#Acá se está tomando todo en minúsculas
print(animal.lower())
#Acá la primera letra de la cadena de texto se está tomando en mayúsculas, las demás en minúsculas
print(animal.capitalize())
#Acá lo que hace el siguiente método es tomar la primera letra de cada palabra y convertirlas en mayúsculas
print(animal.title())
#Acá lo que hace es tomar los espacios en blanco a la izquierda y derecha del texto
print(animal.strip())

#Nota: Los métodos se pueden poner consecutivamente, ejemplo:
print(animal.strip().capitalize())
#Ahí lo que sucedió es que se imprime la cadena "Chanchito Feliz" pero sin ningún espacio a los bordes y con las primeras letras de cada palabra en mayúsculas

#El siguiente método lo que hace es buscar una cadena de caracteres que le indiquemos y nos devuelve el íncdice
print(animal.find("ch"))

#Este método remplaza un caracter en especifico al pasarle un valor en concreto, es decir que si hay una palbra que 
#contenga "J" y le doy un valor "S", "J" será reemplazado
print(animal.replace("IT", "j"))

#Este devuelve un booleano, puesto que se le está preguntando si es cierto o falso
print("IT" in animal)

print("IT" not in animal)