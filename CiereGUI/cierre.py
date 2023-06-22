from funciones import *
from motivos import incidente, medio, diagnostico
import os 
from tkinter import *
import webbrowser




def cleanScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    cleanScreen()
    root = Tk()

    root.geometry("800x400")

    labelRadicado = Label(root, text="Radicado:")
    labelRadicado.place(x=50, y=75)

    enterRadicado = Entry(root, fg = "black")
    enterRadicado.place(x=150, y=75)

    radicado = enterRadicado.get()
    url = f'https://mesadeservicio.autonoma.edu.co/avance/crear/{radicado}'
    

    labelNombre = Label(root, text="Nombre:")
    labelNombre.place(x=50, y=100)

    enterNombre = Entry(root, fg = "black")
    enterNombre.place(x=150, y=100)

    send = Button(root, text="Enviar", command=buscador())
    send.place(x=200, y=300)
    

    root.mainloop()



def buscador():

    webbrowser.open_new(url)

main()












