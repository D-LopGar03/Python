"""
Crear un programa que reciba el nombre de 3 trabajadores y pregunte cuantos días faltaron e imprima en orden descendente quien faltó más 
"""

# Listas para almacenar los datos
trabajadores = []
dias_faltados = []

def recibir_datos():
    # Recibir el nombre y los días faltados para 3 trabajadores
    for _ in range(3):  # Solo necesitamos 3 trabajadores
        trabajador = input("Ingrese el nombre del trabajador: ")
        trabajadores.append(trabajador)
        dias = int(input("Ingrese la cantidad de días faltados: "))  # Convertimos la entrada a entero
        dias_faltados.append(dias)

def ordenar_y_mostrar():
    # Usamos zip para combinar trabajadores y días faltados
    trabajadores_dias = list(zip(trabajadores, dias_faltados))

    # Ordenamos por los días faltados en orden descendente
    trabajadores_dias.sort(key=lambda x: x[1], reverse=True)

    # Mostramos el nombre del trabajador y los días faltados en orden descendente
    print("\nOrden de los trabajadores según los días faltados (de más a menos):")
    for trabajador, dias in trabajadores_dias:
        print(f"{trabajador} faltó {dias} días")

# Ejecutar los pasos
recibir_datos()  # Llamamos para recibir la entrada de los usuarios
ordenar_y_mostrar()  # Ordenamos e imprimimos los resultados


    
