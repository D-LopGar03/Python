# El método strip se utiliza para eliminar caracteres especificados al inicio y final de una cadena de
# caracteres, tomando en cuenta que si al método strip no se le especifica uno o más caracteres,
# solo eliminará espacios en blanco y saltos de línea

# Este método solo elimina caracteres al inicio y al final de una cadena de caracteres, pero no en la parte 
# central de la cadena

cadena = "\tHola Damian\n"
print(cadena)

# Eliminar caracteres especificados de una cadena

cadena = cadena.strip("anHo \t \n")
print(cadena)

# Eliminar saltos de líneas, espacios en blanco y tabulaciones

cadena = cadena.strip()
print(cadena)



# El método rstrip se utiliza para eliminar únicamente caracteres especificados al final de una cadena,
# al igual que el método strip, si no se especifica un caracter a eliminar, solo eliminará espacios en 
# blanco y saltos de línea

string = "\tHola Ernesto\n"
print(string)

string = string.rstrip("s tHo\t \n")
print(string)

# El método lstrip se utiliza para eliminar únicamente caracteres especificados al inicio de una cadena,
# al igual que el método strip, si no se especifica un caracter a eliminar, solo eliminará espacios en 
# blanco y saltos de línea

string = " \t\tBuenas \n"
string = string.lstrip("B ue\t \n")
print(string)