from tkinter import *
from funciones import *
from motivos import incidente, diagnostico, medio, solucion
from tkinter import ttk

def obtenerDatos():
    radicado = cajaRadicado.get()
    user = cajaNombre.get()
    user = user.title()
    opcionIncidente = comboIncidente.get()
    opcionDiagnostico = comboDiagnostico.get()
    recibirDatos(radicado, user, opcionIncidente, opcionDiagnostico)


root = Tk()

root.geometry("800x300")

labelRadicado = Label(root, text="Radicado:")
labelRadicado.place(x=50, y=50)
cajaRadicado = Entry(root)
cajaRadicado.place(x=150, y=50)

labelNombre = Label(root, text="Nombre:")
labelNombre.place(x=50, y=75)
cajaNombre = Entry(root)
cajaNombre.place(x=150, y=75)

labelIncidente = Label(root, text="Incidente: ")
labelIncidente.place(x=50, y=100)

opcionesIncidente = list(incidente.values())
llaveIncidente = list(incidente.keys())
comboIncidente = ttk.Combobox(root, values=opcionesIncidente, width=60)
comboIncidente.place(x=150, y=100)

labelDiagnostico = Label(root, text="Diagnostico: ")
labelDiagnostico.place(x=50, y=125)

opcionesDiagnostico = list(diagnostico.values())
comboDiagnostico = ttk.Combobox(root, values=opcionesDiagnostico, width=60)
comboDiagnostico.place(x=150, y=125)


send = Button(root, text="Enviar", command=obtenerDatos)
send.pack(side="bottom")

root.mainloop()
