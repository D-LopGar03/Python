from tkinter import *
import Eleccion

def llamarPiedra():
    Eleccion.piedra()

def llamarPapel():
    Eleccion.papel()

def llamarTijera():
    Eleccion.tijera()

# Crear una instancia de la ventana
root = Tk()
root.resizable(0, 0)
root.geometry("800x450")
root.config(bg="black")
root.title("Piedra, Papel o Tijera")

# Cargar la imagen de la piedra
piedra = PhotoImage(file="images/piedra.png")

# Redimensionar la imagen de la piedra

piedraRedimensionada = piedra.subsample(13,13)

# Crear el botón con la piedra
botonPiedra = Button(root, image=piedraRedimensionada, command=llamarPiedra)
botonPiedra.place(x=50, y=25)

# Cargar la imagen de la tijera

tijera = PhotoImage(file="images/tijera.png")

# Redimensionar la imagen de la tijera

tijeraRedimensionada = tijera.subsample(13,13)

# Crear el botón con la piedra
botonTijera = Button(root, image=tijeraRedimensionada, command=llamarTijera)
botonTijera.place(x=50, y=150)

# Cargar la imagen del papel

papel = PhotoImage(file="images/papel.png")

# Redimensionar la imagen del papel

papelRedimensionado = papel.subsample(21, 15)

# Crear el boton del papel

botonPapel = Button(root, image=papelRedimensionado, command=llamarPapel)
botonPapel.place(x=50, y=275)

# Iniciar el bucle de eventos
root.mainloop()

