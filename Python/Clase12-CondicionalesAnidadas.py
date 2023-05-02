import time

def introducing():
    print("\t==========\n\tConversor\n\t==========\nMenú de opciones:\n")

    print("Presiona 1 para convertir de números a letras.\nPresiona 2 para convertir de letras a números.\n")
    opc = int(input("¿Qué opción eliges?: "))
    option(opc)

def option(opc):
    if opc == 1:
        print("Conversor de número a palabra.")
        num = int(input("Ingresa un número entre 0 y 10: "))
        if num == 0:
            print("Este número es 'Cero'.")
        elif num == 1:
            print("Este número es 'Uno'.")
        elif num == 2:
            print("Este número es 'Dos'.")
        elif num == 3:
            print("Este número es 'Tres'.")
        elif num == 4:
            print("Este número es 'Cuatro'.")
        elif num == 5:
            print("Este número es 'Cinco'.")
        elif num == 6:
            print("Este número es 'Seis'.")
        elif num == 7:
            print("Este número es 'Siete'.")
        elif num == 8:
            print("Este número es 'Ocho'.")
        elif num == 9:
            print("Este número es 'Nueve'.")
        elif num == 10:
            print("Este número es 'Diez'.")
        else:
            print("Este número no está dentro de las opciones contempladas")

    elif opc == 2:
        print("Conversor de palabra a número.")
        pal = str(input("Ingresa un número como palabra, máximo 5, 'Ejemplo: Uno': "))
        pal = pal.lower()
        if pal == "uno":
            print("1")
        elif pal == "dos":
            print("2")
        elif pal == "tres":
            print("3")
        elif pal == "cuatro":
            print("4")
        elif pal == "cinco":
            print("5")
        else:
            print("Esta palabra no está dentro de las opciones contempladas.")
    else:
        print("Opción inválida.")
        time.sleep(2.5)
        introducing()

introducing()