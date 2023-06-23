import webbrowser, time, datetime, pyautogui, pyperclip, os
from motivos import *

def recibirDatos(radicado, user, opcionIncidente, opcionDiagnostico):
    url = f"https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}"
    interactuarBuscador(url)

    for index in incidente:
        if index == opcionIncidente:
            print("La opción es: ")
        else:
            print(index)

    time.sleep(3)

    for i in range(0, 9):
        pyautogui.hotkey('tab')
    
    
def interactuarBuscador(url):
    webbrowser.open_new_tab(url)


