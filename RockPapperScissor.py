import random
import os

from os import system
system("cls")

selectUser = input(str("Piedra, papel o tijeras: "))
selectUserModify = selectUser.lower()

opciones = ['Papel', 'Piedra', 'Tijeras']

seleccion = (random.choice(opciones))
seleccionModify = seleccion.lower()

#POSIBLES SELECCIONES DEL USUARIO CON PIEDRA

if selectUserModify == "piedra" and seleccion == "Piedra":
    print(selectUserModify, " vs ", seleccionModify)
    print("Empate")        
elif selectUserModify == "piedra" and seleccion == "Papel":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo gano")
elif selectUserModify == "piedra" and seleccion == "Tijeras":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo pierdo")

#POSIBLES SELECCIONES DEL USUARIO CON PAPEL

elif selectUserModify == "papel" and seleccion == "Papel":
    print(selectUserModify, " vs ", seleccionModify)
    print("Empate") 
elif selectUserModify == "papel" and seleccion == "Piedra":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo pierdo")
elif selectUserModify == "papel" and seleccion == "Tijeras":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo gano")

#POSIBLES SELECCIONES DEL USUARIO CON TIJERAS

elif selectUserModify == "tijeras" and seleccion == "Papel":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo pierdo") 
elif selectUserModify == "tijeras" and seleccion == "Piedra":
    print(selectUserModify, " vs ", seleccionModify)
    print("Yo gano")
elif selectUserModify == "tijeras" and seleccion == "Tijeras":
    print(selectUserModify, " vs ", seleccionModify)
    print("Empate")

