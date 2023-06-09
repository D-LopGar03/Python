import pyperclip
import webbrowser 
import pyautogui
import datetime

hora_actual = datetime.datetime.now().time()

hora_inicio_tarde = datetime.time(12, 0, 0)
hora_inicio_noche = datetime.time(18, 0, 0)  

if hora_actual < hora_inicio_tarde:
    tiempo = "tarde"
elif hora_actual < hora_inicio_noche:
    tiempo = "día"


print("Cierre de mesa")

solicitud = int(input("Número de radicado: "))

def opciones():
    choice=int(input(f"1). Activación de Office.\n2). Revisión de red.\n3). Optimización del equipo.\n> "))
    seleccion(choice)

def seleccion(choice):
    if choice == 1:
                
        if tiempo == "día":
            username = str(input("¿Cómo se llama el usuario?: "))
            username = username.capitalize()
            cierreOffice(username, tiempo)

        elif tiempo == "tarde":
            username = str(input("¿Cómo se llama el usuario?: "))
            username = username.capitalize()
            cierreOffice(username, tiempo)
        else:
            print("Opción no encontrada...")
            seleccion(choice)

def cierreOffice(username, tiempo):

    if tiempo == "día":
        with open("texto.txt", "w") as o:
            o.write((f"Buenos días, {username}\n\nSe realiza la activación de la licencia de Office para su correcto funcionamiento.\n\nFeliz día."))
    elif tiempo == "tarde":
        print(f"Buenas tardes, {username}\n\nSe realiza la activación de la licencia de Office para su correcto funcionamiento.\n\nFeliz tarde.")

def openBrowser(solicitud):
    webbrowser.open_new(f"https://mesadeservicio.autonoma.edu.co/avance/crear/{solicitud}")
    documento = open("texto.txt", "r")
    pyautogui.position(900, 30)
    
    for i in documento:
        pyperclip.copy(i)      
        pyautogui.hotkey("ctrl", "v")
    


opciones()
openBrowser(solicitud)