import webbrowser, time, datetime, pyautogui, pyperclip, os
from motivos import *

archivo = 'documento'

def cleanScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def horas(opcionIncidente, user, archivo):

    hora_actual = datetime.datetime.now().time()
    tarde = datetime.time(12, 0, 0)
    noche = datetime.time(19, 0, 0) 

    if hora_actual < tarde:

        saludo = "Buenos días"
        cuerpo = str(solucion[opcionIncidente])
        despedida = "Feliz día"
        interactuarDocumento(archivo, saludo, cuerpo, despedida, user)

    elif hora_actual < noche:
        
        saludo = "Buenas tardes"
        cuerpo = str(solucion[opcionIncidente])
        despedida = "Feliz tarde"
        interactuarDocumento(archivo, saludo, cuerpo, despedida, user)
    else:

        saludo = "Buenas noches"
        cuerpo = str(solucion[opcionIncidente])
        despedida = "Feliz noche"
        interactuarDocumento(archivo, saludo, cuerpo, despedida, user)

def recibirDatos(radicado, opcionIncidente, opcionDiagnostico, user):

    url = f"https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}"
    interactuarBuscador(url, opcionIncidente, user)

    time.sleep(3)

    for i in range(0, 9):
        pyautogui.hotkey('tab')

def interactuarDocumento(archivo, user, saludo, cuerpo, despedida):
    with open(archivo, 'w') as file:
        file.write(f"{saludo}, {user}\n\n{cuerpo}, \n\n{despedida}")


def interactuarBuscador(url, opcionIncidente, user):
    horas(opcionIncidente, user, archivo)

    webbrowser.open_new_tab(url)


