import time
import random
from colorama import Fore, Back, Style

estado = False
acelerometro = ""

frases = ["Este reciente fallecimiento nos ha dejado impresionados. Les acompañamos en el sentimiento.", "Ante estas circunstancias tan difíciles sólo puedo orar para que tengas consuelo y no te desesperes más por esta pérdida irreparable. Puedes contar conmigo para lo que desees y te envío mis más sinceras condolencias.", "Apenas me acabo de enterar del lamentable fallecimiento. Dios le ayude a soportar tan gran ausencia.", "El motivo de este mensaje es expresarle mis más profundas condolencias por el reciente fallecimiento.\nDeseo que su alma descanse en paz y que encuentren pronto la resignación por tan enorme pérdida.", "Es triste, aunque es ley de vida, la muerte llega cuando menos la esperamos."]

def encender():
    eleccion = str(input("¿Encender coche? s/n: "))
    if eleccion == "s":
        encendido()
    else:
        print(Fore.GREEN, "Ok, saliendo del coche", Fore.RESET)

def encendido():
    acelerometro = 0
    estado = True
    time.sleep(2.5)
    print(Fore.GREEN, "Coche encendido, calentando el motor...", Fore.RESET)
    time.sleep(2.5)
    aceleramos = str(input("¿Aceleramos? s/n: "))
    if aceleramos == "s":
        acelerar()
    else:
        noAcelerar()

def acelerar():
    acelerometro = 0
    while acelerometro < 100:
        acelerometro = acelerometro + 10
        print("Acelerando")        
        print(acelerometro, " km/h")
        time.sleep(0.7)
    print(Fore.YELLOW)
    eleccion = str(input("¿Deseas frenar? s/n: "))
    print(Fore.RESET)

    if eleccion == "s":
        frenar(acelerometro)
    else:
        nofrenar(acelerometro)

def nofrenar(acelerometro):
    acelerando = acelerometro
    while acelerando <= 220:
        acelerando = acelerando + 10
        print("Acelerando")        
        print(acelerando, " km/h")
        time.sleep(0.3)
    acelerometro = acelerando
    print(Fore.RED)
    eleccion = str(input("Estás excedidendo los límites de velocidad... ¿Deseas frenar ahora mismo? s/n: "))
    print(Fore.RESET)

    if eleccion == "n":
        time.sleep(5)
        badEnding()
    else:
        frenar(acelerometro)

def frenar(acelerometro):
    desaceleracion = acelerometro

    while desaceleracion > 150:
        desaceleracion = desaceleracion - 10
        print ("Frenando")
        time.sleep(0.8)
        print(desaceleracion, " km/h")
    
    if desaceleracion >= 150:
        print(Fore.YELLOW)
        eleccion = str(input("¿Deseas continuar el recorrido? s/n: "))
        print(Fore.RESET)
        if eleccion == "s":
            for i in range(4):
                print(desaceleracion, " km/h")
                time.sleep(1.5)
            acelerometro = desaceleracion    
            frenadoTotal(acelerometro)
        else:
            acelerometro = desaceleracion
            apagado(acelerometro)
    else:
        while desaceleracion > 0:
            desaceleracion = desaceleracion - 10
            print ("Frenando")
            time.sleep(0.8)
            print(desaceleracion, " km/h")
        acelerometro = desaceleracion
        apagado(acelerometro)


def frenadoTotal(acelerometro):
    desaceleracion = acelerometro
    while desaceleracion > 0:
        desaceleracion = desaceleracion - 10
        print ("Frenando")
        time.sleep(0.5)
        print(desaceleracion, " km/h")    
    acelerometro = desaceleracion    
    apagado(acelerometro)


def apagado(acelerometro):
    desaceleracion = acelerometro

    while desaceleracion > 0:
        desaceleracion = desaceleracion - 10
        print ("Frenando")
        time.sleep(0.5)
        print(desaceleracion, " km/h")    
    acelerometro = desaceleracion      

    print(Fore.YELLOW)
    apagar = str(input("Has llegado a tu destino, ¿Deseas apagar el coche? s/n: "))
    print(Fore.RESET)
    if apagar == "s":
        print (Fore.GREEN, "Apagando coche")
        estado = False
        time.sleep(2.5)
        print("Coche apagado con éxito, ten un buen día", Fore.RESET) 
    else:
        eleccion = str(input(f"Entonces espero hasta que decidas si apagar el coche o no: \n1). Apagar el coche.\n2). Acelerar de nuevo. \n"))
        if eleccion == "1":
            print (Fore.GREEN, "Apagando coche")
            estado = False
            time.sleep(2.5)
            print("Coche apagado con éxito, ten un buen día", Fore.RESET) 
        else:
            acelerar()

def badEnding():
    for index in range(3):
        ded = (random.choice(frases))
        print(ded)
        time.sleep(5)
    print(Fore.RED, "\nHAS MUERTO, RESPETA LOS LÍMITES DE VELOCIDAD...", Fore.RESET)
    
    eleccion = str(input("¿Deseas reiniciar? s/n: "))
    if eleccion == "s":
        encender()
    else:
        print("Ok, saliendo del juego")
        exit()
        
def noAcelerar():
    eleccion = str(input(f"Entonces espero hasta que decidas si apagar el coche o no: \n1). Apagar el coche.\n2). Acelerar. \n"))
    if eleccion == "1":
        print (Fore.GREEN, "Apagando coche")
        estado = False
        time.sleep(2.5)
        print("Coche apagado con éxito, ten un buen día", Fore.RESET) 
    else:
        acelerar()

encender() 
