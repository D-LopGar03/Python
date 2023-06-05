# El método swapcase() en Python es una función de cadena que invierte las mayúsculas y minúsculas de los 
# caracteres en una cadena. Cambia todas las letras mayúsculas a minúsculas y todas las letras minúsculas a mayúsculas, 
# mientras mantiene los caracteres no alfabéticos sin cambios.

texto = "hOLA mUNDO"
print("Cadena modificada:",texto.swapcase()) # Cambia las mayúsculas por minúsculas y viceversa
print("Cadena original:", texto)

numbers = "1234***-"
print(numbers.swapcase()) # No afecta a los simbolos o números
