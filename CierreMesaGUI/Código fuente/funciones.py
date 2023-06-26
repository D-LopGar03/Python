import time, pyautogui, pyperclip, datetime, webbrowser
from motivos import *

hora_actual = datetime.datetime.now().time()
tarde = datetime.time(12, 0, 0)
noche = datetime.time(19, 0, 0) 

# Recibimos los datos del archivo cierre ya verificados sus campos y editamos una URL

def recibirDatos(radicado, user, motivo, diagnostico, medio):
    url = f"https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}"
    buscador(url)
    crearDocumento(motivo, user)
    interactuarBuscador(medio, diagnostico)

# Abrimos una nueva pestaña del navegador con la URL ya definida anteriormente

def buscador(url):
    webbrowser.open_new(url)
        
# Nos movemos por los campos específicos de la página web ya abierta

def interactuarBuscador(medio, diagnostico):

    time.sleep(3)
    for tab in range(0, 9):
        pyautogui.hotkey('tab')
    
    for down in range(medio):
        pyautogui.hotkey('down')
    
    pyautogui.hotkey('tab')

    for down in range(diagnostico):
        pyautogui.hotkey('down')

    for tab in range(0, 4):
        pyautogui.hotkey('tab')

    leerDocumento()

    for tab in range(0, 2):
        pyautogui.hotkey('tab')
    
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')

# Creamos un nuevo documento definiendo su saludo, que este depende de la hora, ya sea
# día, tarde o noche, recibe el nombre del usuario y a partir del incidente llamado motivo como
# valor numérico dentro del diccionario incidente, valida que tipo respuesta dar y al final da su
# despedida, que se define en día, tarde o noche 

def crearDocumento(motivo, user):

    if hora_actual < tarde:
        saludo = "Buenos días"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz día."
        with open('documento', 'w') as file:
            file.write(f"{saludo}, {user}\n\n{cuerpo}\n\n{despedida}")
    elif hora_actual < noche: 
        saludo = "Buenas tardes"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz tarde."
        with open('documento', 'w') as file:
            file.write(f"{saludo}, {user}\n\n{cuerpo}\n\n{despedida}")
    else:
        saludo = "Buenas noches"
        cuerpo = str(solucion[motivo])
        despedida = "Feliz noche."
        with open('documento', 'w') as file:
            file.write(f"{saludo}, {user}\n\n{cuerpo}\n\n{despedida}")

# Leemos el documento anterior para posteriomente, junto a la interacción con el buscador,
# copie y pegue cada una de las líneas presentes en este

def leerDocumento():
    for linea in open('documento', 'r'):
        pyperclip.copy(linea)
        pyautogui.hotkey('ctrl', 'v')