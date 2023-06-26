from funciones import *
from motivos import incidente, medio, diagnostico
from colorama import Fore, Style, Back, init
import os 

init()

def cleanScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

cleanScreen()

radicado = int(input(f"{Back.WHITE} * {Back.RESET}{Back.CYAN}{Fore.BLACK} Número del radicado de la solicitud:{Fore.RESET}{Back.RESET} ")) 

user = (input(f"\n{Back.WHITE} * {Back.RESET}{Back.CYAN}{Fore.BLACK} Nombre del usuario:{Fore.RESET}{Back.RESET} "))

user = user.title()

print(f"\n{Back.WHITE} * {Back.RESET}{Back.CYAN}{Fore.BLACK} Incidente\n\n{Fore.RESET}{Back.RESET}")

for i in range(1, len(incidente) + 1, 2):

    print(incidente[i], end="\t\t\t")

    if i + 1 in incidente:
        print(incidente[i + 1])
        print("\n")
    
motivo = int(input(f"\n\n{Back.WHITE}>{Back.RESET} "))

print(f"\n{Back.WHITE} * {Back.RESET}{Back.CYAN}{Fore.BLACK} Medio de atención{Fore.RESET}{Back.RESET}\n ")

for place in range(1, len(medio) + 1, 2):

    print(medio[place], end='\t\t\t')
    
    if place + 1 in medio:
        print(medio[place + 1])
        print("\n")
    
   

lugar = int(input(f"\n\n{Back.WHITE}>{Back.RESET} "))

print(f"\n{Back.WHITE} * {Back.RESET}{Back.CYAN}{Fore.BLACK} Diagnostico{Fore.RESET}{Back.RESET}\n ")

for dictam in range(1, len(diagnostico) + 1, 2):

    print(diagnostico[dictam], end='\t\t\t')
    
    if dictam + 1 in diagnostico:
        print(diagnostico[dictam + 1])
    else:
        ("\n")

eleccion = int(input(f"\n\n{Back.WHITE}>{Back.RESET} "))