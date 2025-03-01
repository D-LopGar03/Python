# El método tittle convierte la primera letra de una cadena en mayúscula y las demás en minúsculas
# y el método istittle verifica si la primera letra es mayúscula y retorna falso o verdadero

def entrada():
    nombre = str(input("Ingresa tu nombre: "))
    comparar = nombre.istitle()

    if comparar == False:
        convertir(nombre)
    else:
        print("El nombre está escrito correctamente")

def convertir(nombre):
    print(nombre.title())

entrada()