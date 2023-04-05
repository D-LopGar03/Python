import random

num = 0 

def bienvenida():
    print("Ingresa un número de 4 cifras para jugar a la lotería")
    num = int(input())
    jugar()

def jugar():
    loteria = random.randint(0000, 9999)
    if loteria == num:
        print("Has ganado")
    else:
        print("Has perdido, el número ganador era ", loteria)
 
bienvenida()