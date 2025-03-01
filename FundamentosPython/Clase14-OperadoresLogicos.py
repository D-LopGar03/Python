""" num_uno =  8
num_dos = 5

def conjunto():
    #VALIDA SI AMBOS ARGUMENTOS SE CUMPLEN
    if num_uno == 5 and num_dos >= 5:
        print("Ambas condiciones son verdaderas")
    else:
        print("Una o ambas condiciones no se han cumplido")

def disyuncion():
    #VALIDA SI CUALQUIERA DE LOS DOS SE CUMPLEN
    if num_uno == 5 or num_dos >= 5:
        print("Una o ambas condiciones se han cumplido")
    else:
        print("Ninguna condición se ha cumplido")

def negacion():
    #NIEGA EL O LOS ARGUMENTOS DADOS
    if not num_uno > 5:
        print("Me imprimo porque soy un valor menor o igual a 5")
    else:
        print("Me imprimo porque soy mayor a 5")
 """

 #Conjunción

def conjuncion():
    print("Conjunción (and)")

    num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

    if num_uno > 2 and num_uno < 5:
        print("El número", num_uno,"cumple la condición de ser menor a 5 y mayor a 2")
    else:
        print(num_uno,"no cumple con las condiciones espectadas, escribe nuevamente el número")
        conjuncion()

conjuncion()

#Disyunción

def disyuncion():
    print("Disyunción (or)")

    palabra = str(input("Para cumplir con la condición escribe 'si' o 'yes': "))

    if palabra == "si" or palabra == "yes":
        print("La condición se ha cumplido.")
    else:
        print("La condición no se ha cumplido, repitelo nuevamente.")
        disyuncion() 

disyuncion()

#Negación

def negar():
    print("Negación (not)")

    num_uno = int(input("Introduce un número igual a 5: "))
    if not num_uno == 5:
        print("El número es diferente a 5 y SI cumple la condición.")
    else:
        print("El número es igual a 5 y NO cumple la condición.")
negar()

