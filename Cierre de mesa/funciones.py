from cierre import user, motivo, radicado
from motivos import motivos
import webbrowser, datetime, sys, pyautogui, pyperclip, time


path = 'documento'

hora_actual = datetime.datetime.now().time()

# Definir los límites para "buenos días" y "buenas tardes"
hora_inicio_tarde = datetime.time(12, 0, 0)  # Por ejemplo, a partir de las 12:00:00 se considera "tarde"
hora_inicio_noche = datetime.time(23, 0, 0)  # Por ejemplo, a partir de las 18:00:00 se considera "noche"

# Comparar la hora actual con los límites
if hora_actual < hora_inicio_tarde:
    hora = f"Buenos días, {user}\n\n"
    despedida = ("\n\nFeliz día.")
elif hora_actual < hora_inicio_noche:
    hora = f"Buenas tardes, {user}\n\n"
    despedida = ("\n\nFeliz tarde.")
else:
    hora = f"Buenas noches, {user}\n\n"
    despedida = ("\n\nFeliz noche.")

def concatenar(hora, motivo, despedida, path):

    if motivo == 1 and hora_actual < hora_inicio_tarde:

        hora = str(hora)
        despedida = str(despedida)
        sys.stdout = open(path, 'w')
        print(f"{hora}{motivos[1]}{despedida}")
       

    elif motivo == 1 and hora_actual < hora_inicio_noche:
                  
         hora = str(hora)
         despedida = str(despedida)
         sys.stdout = open(path, 'w')
         print(f"{hora}{motivos[1]} {despedida}")
         
    

concatenar(hora, motivo, despedida, path)



def buscador(radicado):
    webbrowser.open_new(f"https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}")
    time.sleep(3)

buscador(radicado)

def abrirDoc(path='documento'):
    with open('documento', 'r'):
        for i in path:
            pyperclip.copy(i)

abrirDoc(path)

exit(0)