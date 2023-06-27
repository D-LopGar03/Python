from tkinter import *
from tkinter import PhotoImage

def main():
    # Crear una instancia de la ventana
    root = Tk()
    root.geometry("800x450")
    root.config(bg="black")
    root.title("Piedra, Papel o Tijera")

    # Cargar la imagen de la piedra
    piedra = PhotoImage(file="images/piedra.png")

    # Redimensionar la imagen de la piedra

    piedraRedimensionada = piedra.subsample(13,13)

    # Crear el botón con la piedra
    botonPiedra = Button(root, image=piedraRedimensionada)
    botonPiedra.place(x=50, y=25)

    # Cargar la imagen de la tijera

    tijera = PhotoImage(file="images/tijera.png")

    # Redimensionar la imagen de la tijera

    tijerRedimensionada = tijera.subsample(13,13)

    # Crear el botón con la piedra
    botonTijera = Button(root, image=tijerRedimensionada)
    botonTijera.place(x=50, y=150)

    # Cargar la imagen del papel

    papel = PhotoImage(file="images/papel.png")

    # Redimensionar la imagen del papel

    papelRedimensionado = papel.subsample(21, 15)

    # Crear el boton del papel

    botonPapel = Button(root, image=papelRedimensionado)
    botonPapel.place(x=50, y=275)

    # Iniciar el bucle de eventos
    root.mainloop()

main()
