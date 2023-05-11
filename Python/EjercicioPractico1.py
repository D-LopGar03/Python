#SISTEMA VACACIONAL RAPPI

#CLAVE 1 ATENCIÓN AL CLIENTE
#CLAVE 2 LOGÍSTICA
#CLAVE 3 GERENCIA

print ("\t---------------------------\n\tSISTEMA VACACIONAL DE RAPPI\n\t---------------------------\n\n")

name = str(input("¿Cómo se llama el trabajador?: "))
print("Escoge el departamento al cuál", name, "pertenece\n\t1). CLAVE 1 o atención al cliente\n\t2). CLAVE 2 o logística\n\t3). CLAVE 3 o gerencia")

choice = str(input())
choice = choice.lower()

def eleccion():
    if choice == "1" or choice == "clave 1" or choice == "atención al cliente":
        years = float(input("¿Cuántos años lleva con la empresa?: "))
    if years < 0:
        print ("Los años no pueden ser negativos, ingresa un valor válido.")
    

    if years >= 1 and years < 2 and years < 6 and years < 7:
        print(name,"merece 6 días de vacaciones.")  
    elif years >= 2 and years <= 6 and years < 7:
        print(name,"merece 14 días de vacaciones.") 
    elif years >= 7:
        print(name,"merece 20 días de vacaciones")
    elif years == 0 or years < 1:
        print(name,"no merece vacaciones")

