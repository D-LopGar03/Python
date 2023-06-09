import random
import os
import shutil

x = 1000

def linux(x):
    while x >= 6:
        resta = x - 7
        answr = int(input(f"¿Cuánto es {x} - 7?: "))
        while answr != resta:
            answr=int(input(f"Voy a borrar algún archivo si fallas, ¿cuánto es {x} - 7?: "))
            if random.randint(1, 2)==1:
                try:
                    shutil.rmtree("/home/ay4t0/Escritorio/Example")
                except:
                    print("No")
            
        x = resta

def iniciar():
        if os.name == "nt":
            os.system("cls")
        else:
            linux(x)

iniciar()



