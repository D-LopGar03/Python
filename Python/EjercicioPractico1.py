#SISTEMA VACACIONAL RAPPI

#CLAVE 1 ATENCIÓN AL CLIENTE
#CLAVE 2 LOGÍSTICA
#CLAVE 3 GERENCIA

print ("\t---------------------------\n\tSISTEMA VACACIONAL DE RAPPI\n\t---------------------------\n\n")


def inicio():
    name = str(input("¿Cómo se llama el trabajador?: "))
    print("Escoge el departamento al cuál", name, "pertenece\n\t1). CLAVE 1 o atención al cliente\n\t2). CLAVE 2 o logística\n\t3). CLAVE 3 o gerencia")

    choice = str(input())
    choice = choice.lower()
    eleccion(choice, name)

def eleccion(choice, name):

    if choice == "1" or choice == "clave 1" or choice == "atención al cliente":
        years = float(input("¿Cuántos años lleva con la empresa?: "))
        if years < 0:
            print("Los años no pueden ser negativos")
            eleccion(choice, name)

        def clave1(years):
            if years >= 1 and years < 2 and years < 6 and years < 7:
                print(name,"merece 6 días de vacaciones.")  
            elif years >= 2 and years <= 6 and years < 7:
                print(name,"merece 14 días de vacaciones.") 
            elif years >= 7:
                print(name,"merece 20 días de vacaciones")
            elif years == 0 or years < 1:
                print(name,"no merece vacaciones")
        clave1(years)

    elif choice == "2" or choice == "clave 2" or choice == "logística":
        years = float(input("¿Cuántos años lleva con la empresa?: "))

        def clave2(years):
            if years >= 1 and years < 2 and years < 6 and years < 7:
                print(name,"merece 7 días de vacaciones.")  
            elif years >= 2 and years <= 6 and years < 7:
                print(name,"merece 15 días de vacaciones.") 
            elif years >= 7:
                print(name,"merece 22 días de vacaciones")
            elif years == 0 or years < 1:
                print(name,"no merece vacaciones")
        clave2(years)

    elif choice == "3" or choice == "clave 3" or choice == "gerencia":
        years = float(input("¿Cuántos años lleva con la empresa?: "))

        def clave3(years):
            if years >= 1 and years < 2 and years < 6 and years < 7:
                print(name,"merece 10 días de vacaciones.")  
            elif years >= 2 and years <= 6 and years < 7:
                print(name,"merece 20 días de vacaciones.") 
            elif years >= 7:
                print(name,"merece 30 días de vacaciones")
            elif years == 0 or years < 1:
                print(name,"no merece vacaciones")
        clave3(years)
    
inicio()