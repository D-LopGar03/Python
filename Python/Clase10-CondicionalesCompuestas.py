print("Sistema para calcualar promedios: ")

nombre = str(input("Nombre: "))

math = float(input("Nota para matemáticas: "))
chemestry = float(input("Nota para química: " ))
physyc = float(input("Nota para física: "))

promedio = math + chemestry + physyc / 3 

if promedio >= 6:
    print("Felicidades", nombre, '"aprobaste" con un promedio de ', promedio)
    print("Felicidades", nombre, '"aprobaste" con un promedio de ', round(promedio,2))
else:
    print("No aprobaste", nombre, 'tu promedio fue de ', promedio)