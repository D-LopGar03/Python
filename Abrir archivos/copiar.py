import pyautogui, pyperclip, webbrowser, time, sys

nombre = str(input("Nombre del usuario: "))
motivo = str(input("Daño: "))

sys.stdout = open('documento', 'w', encoding="utf-8")
print(f"Hola {nombre}\nTu daño es {motivo}")

def leerDocumento():
    """ documento = open('documento', 'r', encoding="utf-8")
    documento = documento.read().split("\n") """

    sys.stdin()

    
    for linea in documento:
        pyperclip.copy(linea)
        pyautogui.hotkey('ctrl', 'v', interval=0.15)

def abrirBuscador():

    webbrowser.open_new("https://mesadeservicio.autonoma.edu.co/avance/crear/155035")
    time.sleep(3.0)

    for key in range(0, 14):
        pyautogui.hotkey('tab')
    
    leerDocumento()
    
        

abrirBuscador()