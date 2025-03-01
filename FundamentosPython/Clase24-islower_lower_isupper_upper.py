# En python contamos con varios métodos para saber si una cadena está 
# en mayúsculas o minúsculas y también para convertirlas a este tipo

cadena = "hola"
print(cadena,"está escrito en minúsculas")
cadena = cadena.islower() # Retorna true, pues se le dan todas las letras minúsculas en la variable cadena, de lo contrario retornaría false
print(cadena)


cadena = "HOLAAAAA"
print(cadena,": todo en mayúsculas")
cadena = cadena.lower() # Convierte todas las letras de una variable en minúsculas
print("Ahora en minúsculas: ",cadena)

cadena = "Hola"
cadena = cadena.isupper() # Retorna false, pues no todas sus letras están en mayúsculas, de lo contrario sería true
print(cadena)

cadena = "hola"
cadena = cadena.upper() # Convierte todo a mayúsculas
print(cadena)

print("####################################################################")

varCadena = str(input("Ingresa una cadena de texto: "))
print(f"\n¿Todas las letras están en minúsculas?: {varCadena.islower()}")
varCadena = varCadena.lower()
print(f"Ahora en minúsculas: {varCadena}")

print(f"\n¿Todas las letras están en mayúsculas?: {varCadena.isupper()}")
print(f"Ahora en mayúsculas: {varCadena.upper()}")
print(f"Cadena original {varCadena}")
