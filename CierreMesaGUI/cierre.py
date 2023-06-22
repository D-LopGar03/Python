from tkinter import *
from funciones import *
from motivos import incidente
from tkinter import ttk

def obtenerDatos():
    radicado = cajaRadicado.get()
    user = cajaNombre.get()
    user = user.title()
    recibirDatos(radicado, user)


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

for i in incidente:
    index = incidente[i]
    combo = ttk.Combobox(root, values=index)

combo.place(x=150, y=100)



send = Button(root, text="Enviar", command=obtenerDatos)
send.pack(side="bottom")

root.mainloop()