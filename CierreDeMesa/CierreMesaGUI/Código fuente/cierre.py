from tkinter import *
from tkinter import messagebox
from funciones import *
from motivos import *
from tkinter import ttk

# Valida que los datos requeridos estén bien y de ser el caso los corrige

def validarDatos(radicado):
    if any(radicado):
        return True
    else:
        messagebox.showerror("Error", "Ingrese solo valores numéricos en el campo radicado.")
        return False
    
# Una vez ingresados los campos requeridos, los pasa al archivo funciones para comenzar el proceso

def obtenerDatos():

    radicado = cajaRadicado.get()
    validarDatos(radicado)
    user = cajaNombre.get().title()    
    motivo = comboIncidente.current() + 1
    diagnostico = comboDiagnostico.current() + 1
    medio = comboMedio.current() + 1
    recibirDatos(radicado, user, motivo, diagnostico, medio)

# Creamos la instancia de nueva ventana, para más adelante inicializarla

root = Tk()
root.geometry("900x400")
root.title("Cierre de mesa de servicio")
root.resizable(0, 0)
root.config(bg="black")
root.iconbitmap('imagenes/helpDeskLogo.ico')

# Cargar imagen del disco.
imagen = PhotoImage(file="imagenes/logo.png/")

#Se modifica el tamaño de la imagen

new_Image = imagen.subsample(3)

# Insertarla en una etiqueta.
label = ttk.Label(image=new_Image)
label.place(x=0, y=0)

# Entrada de radicado

labelRadicado = Label(root, text="Radicado:", bg="black", fg="white")
labelRadicado.place(x=200, y=100)
cajaRadicado = ttk.Entry(root, width=62)
cajaRadicado.place(x=300, y=100)

# Entrada de nombre

labelNombre = Label(root, text="Nombre:", bg="black", fg="white")
labelNombre.place(x=200, y=150)

cajaNombre = Entry(root, width=62)
cajaNombre.place(x=300, y=150)

# Combobox para el incidente

labelIncidente = Label(root, text="Incidente: ", bg="black", fg="white")
labelIncidente.place(x=200, y=200)
opcionesIncidente = list(incidente.values())
comboIncidente = ttk.Combobox(root, values=opcionesIncidente, width=60, state="readonly")
comboIncidente.place(x=300, y=200)

# Combobox para el diagnóstico

labelDiagnostico = Label(root, text="Diagnóstico: ", bg="black", fg="white")
labelDiagnostico.place(x=200, y=250)
opcionesDiagnostico = list(diagnostico.values())
comboDiagnostico = ttk.Combobox(root, values=opcionesDiagnostico, width=60, state="readonly")
comboDiagnostico.place(x=300, y=250)

# Combobox para el medio de atención

labelMedio = Label(root, text="Medio: ", bg="black", fg="white")
labelMedio.place(x=200, y=300)
opcionesMedio = list(medio.values())
comboMedio = ttk.Combobox(root, values=opcionesMedio, width=60, state="readonly")
comboMedio.place(x=300, y=300)

# Creamos un estilo para el botón de enviar

style = ttk.Style()
style.configure("RoundedButton.TButton", relief="raised", background="#BCBCB5", foreground="#000000", borderwidth=3, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#aaaaaa", focusthickness=1, anchor="center")
style.map("RoundedButton.TButton", background=[('active', "#888888"), ('pressed', "#000000")])

# Creamos el botón de enviar

send = ttk.Button(root, text="Enviar", command=obtenerDatos, style="RoundedButton.TButton")
send.place(x= 450, y=350)

# Inicialización de la ventana principal

root.mainloop()