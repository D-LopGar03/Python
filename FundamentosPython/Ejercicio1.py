""" import time
 """
#Crear un programa donde se almacenen los días de la semana, imprimir los valores 
#y también imprimir el valor que el usuario nos especifique


def semana():
    dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    diaUser = str(input("Ingrese el día de la semana: "))
    print("El día que ha escogido para recibir el boletín fue el", diaUser)
    for index in dia:
        print(index)

def semaforo():
    for time in range(1):
        print("Rojo")
        for timeWaitY in range(40000000):
            timeWaitY = timeWaitY + 1
        print("Amarillo")
        for timeWaitG in range(30000000):
            timeWaitG = timeWaitG + 1
        print("Verde")


semaforo() 
semana()

