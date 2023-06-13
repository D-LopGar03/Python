from cierre import user, motivo, radicado
from motivos import motivos
import webbrowser
import datetime

hora_actual = datetime.datetime.now().time()

# Definir los límites para "buenos días" y "buenas tardes"
hora_inicio_tarde = datetime.time(12, 0, 0)  # Por ejemplo, a partir de las 12:00:00 se considera "tarde"
hora_inicio_noche = datetime.time(19, 0, 0)  # Por ejemplo, a partir de las 18:00:00 se considera "noche"

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

def concatenar(hora, motivo, despedida):

    if motivo == 1 and hora_actual < hora_inicio_tarde:

        with open("documento.txt", "w") as f:
            f.write ({hora}, {motivos[1]}, {despedida})
       

    elif motivo == 1 and hora_actual < hora_inicio_noche:
         entradas = str({hora}, {motivos[1]}, {despedida})
         with open("documento.txt", "w") as f:
            f.write (entradas)
         
         print(f)
    

concatenar(hora, motivo, despedida)



def buscador(radicado):
    webbrowser.open_new(f"https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}")
buscador(radicado)

exit(0)