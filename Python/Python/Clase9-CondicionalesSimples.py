import os

def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
clear()

def start():
    print("Sistema para calcular el promedio de un alumno, ten en cuenta que se califica del 1 al 10")
    nombre = str(input("¿Cómo te llamas?: "))
    great(nombre)    

def great(nombre):
    print("Hola " + nombre)
    grades(nombre)

def grades(nombre):
    grade1 = float(input("¿Cuál es tu primera nota?: "))
    grade2 = float(input("¿Cuál es tu segunda nota?: "))

    if grade1 > 10 or grade2 > 10:
        print("Las notas deben ser menores o iguales a 10")
        grade1 = 0 
        grade2 = 0 
        grades(nombre)  
    else:
        media(grade1, grade2, nombre)   

def media(grade1, grade2, nombre):
    med = (grade1 + grade2) / 2
    med = int(med)
    if med >= 6:
        print("Felicidades",nombre, "aprobaste con un promedio de", med)
    else:
        print("Lástima que hayas reprobado,",nombre, "pero puedes mejorar, tu promedio fue",med)

start()

def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

