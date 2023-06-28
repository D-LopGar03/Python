import os, random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox

directorio = 'images/'

def piedra():

    root = Tk()
    root.geometry("0x0")
    root.resizable(0,0)
    
    arhivos = []

    for file in os.listdir(directorio):
        arhivos.append(file)
    
    seleccion = random.choice(arhivos)

    ruta_imagen = (f'images/{seleccion}/')
    imagen = PhotoImage(file=ruta_imagen)

    new_Image = imagen.subsample(13, 13)

    label = ttk.Label(image=new_Image)
    label.place(x=600, y=150)

    if seleccion == 'piedra.png':
        mbox.showinfo(message="Empate", title="")
        label.destroy()
        
    elif seleccion == 'papel.png':
        mbox.showinfo(message="El PC gana", title="")
        label.destroy()

    else:
        mbox.showinfo(message="El JUGADOR gana", title="")
        label.destroy()

    root.destroy()
    
    root.mainloop()

def papel():

    root = Tk()
    root.geometry("0x0")
    root.resizable(0,0)
    arhivos = []

    for file in os.listdir(directorio):
        arhivos.append(file)
    
    seleccion = random.choice(arhivos)

    ruta_imagen = (f'images/{seleccion}/')
    imagen = PhotoImage(file=ruta_imagen)

    new_Image = imagen.subsample(13, 13)

    label = ttk.Label(image=new_Image)
    label.place(x=600, y=150)

    if seleccion == 'piedra.png':
        mbox.showinfo(message="El JUGADOR gana", title="")
        label.destroy()
        
    elif seleccion == 'papel.png':
        mbox.showinfo(message="Empate", title="")
        label.destroy()
    else:
        mbox.showinfo(message="El PC gana", title="")
        label.destroy()

    root.destroy()    
    root.mainloop()
    
def tijera():

    root = Tk()

    root.geometry("0x0")
    root.resizable(0,0)
    arhivos = []

    for file in os.listdir(directorio):
        arhivos.append(file)
    
    seleccion = random.choice(arhivos)

    ruta_imagen = (f'images/{seleccion}/')
    imagen = PhotoImage(file=ruta_imagen)

    new_Image = imagen.subsample(13, 13)

    label = ttk.Label(image=new_Image)
    label.place(x=600, y=150)

    if seleccion == 'piedra.png':
        mbox.showinfo(message="El PC gana", title="")
        label.destroy()
        
    elif seleccion == 'papel.png':
        mbox.showinfo(message="El JUGADOR gana", title="")
        label.destroy()

    else:
        mbox.showinfo(message="Empate", title="")
        label.destroy()
    root.destroy()
    
    root.mainloop()
