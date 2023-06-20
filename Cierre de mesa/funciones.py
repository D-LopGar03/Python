from cierre import radicado, user, motivo, lugar, diagnostico
from motivos import solucion
import webbrowser, time, datetime, pyautogui, pyperclip, os

url = f'https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}'
archivo = 'documento'

hora_actual = datetime.datetime.now().time()
tarde = datetime.time(12, 0, 0)
noche = datetime.time(19, 0, 0) 


def cleanScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def horas(hora_actual, tarde, noche, motivo, archivo):

    if hora_actual < tarde:

        saludo = "Buenos días"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz día"
        interactuarDocumento(archivo, saludo, cuerpo, despedida)

    elif hora_actual < noche:
        
        saludo = "Buenas tardes"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz tarde"
        interactuarDocumento(archivo, saludo, cuerpo, despedida)
    else:

        saludo = "Buenas noches"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz noche"
        interactuarDocumento(archivo, saludo, cuerpo, despedida)

def interactuarBuscador(url):

    webbrowser.open_new(url)

    time.sleep(3)

    for i in range(0, 14):
        pyautogui.hotkey('tab')


def interactuarDocumento(archivo, saludo, cuerpo, despedida):

    interactuarBuscador(url)
    
    with open(archivo, 'w') as file:
        file = file.write(f"{saludo}, {user}\n\n{cuerpo}\n\n{despedida}.")

    with open(archivo, 'r') as file:

        for linea in file:
            pyperclip.copy(linea)
            pyautogui.hotkey('ctrl', 'v')

    for tab in range(0, 16):
        pyautogui.hotkey('tab')

    sitio(lugar)

def sitio(lugar):
    if lugar == 1:
        for key in range(0, 1):
            pyautogui.hotkey('down')
    elif lugar == 2:
        for key in range(0, 2):
            pyautogui.hotkey('down')
    elif lugar == 3:
        for key in range(0, 3):
            pyautogui.hotkey('down')
    elif lugar == 4:
        for key in range(0, 4):
            pyautogui.hotkey('down')
    elif lugar == 5:
        for key in range(0, 5):
            pyautogui.hotkey('down')

def dictamen(diagnostico):

horas(hora_actual, tarde, noche, motivo, archivo)
cleanScreen()

exit()
