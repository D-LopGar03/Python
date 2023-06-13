from cierre import user, motivo
from motivos import motivos

import datetime

hora_actual = datetime.datetime.now().time()

# Definir los límites para "buenos días" y "buenas tardes"
hora_inicio_tarde = datetime.time(12, 0, 0)  # Por ejemplo, a partir de las 12:00:00 se considera "tarde"
hora_inicio_noche = datetime.time(18, 0, 0)  # Por ejemplo, a partir de las 18:00:00 se considera "noche"

# Comparar la hora actual con los límites
if hora_actual < hora_inicio_tarde:
    hora = (f"Buenos días, {user}\n\n")
    despedida = ("\n\nFeliz día.")
elif hora_actual < hora_inicio_noche:
    hora = (f"Buenas tardes, {user}\n\n")
    despedida = ("\n\nFeliz tarde.")
else:
    hora = (f"Buenas noches, {user}\n\n")
    despedida = ("\n\nFeliz noche.")

def concatenar(motivo, hora, despedida):
    if motivo == 1 and hora_actual < hora_inicio_tarde:
        o = open("documento.txt", "w")
        entradas = print(hora, motivos[1],despedida, sep="")
        o.write(entradas)

    elif motivo == 1 and hora_actual < hora_inicio_noche:
        o = open("documento.txt", "w")
        entradas = print(hora, motivos[1],despedida, sep="")
        o.write(entradas)
    

concatenar(motivo, hora, despedida)

exit(0)