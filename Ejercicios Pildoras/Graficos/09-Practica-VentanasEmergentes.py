
from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Roger", "Procesador de texto versión 2025")   

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")  

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

    if valor==True:
        root.destroy() 

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

    if valor==False:
        root.destroy()

root.title("Aplicación de escritorio")  # Agregar título a la ventana
root.geometry("800x600")  # Establecer tamaño de la ventana

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoArchivo=Menu(barraMenu, tearoff=0)
archivoArchivo.add_command(label="Nuevo")
archivoArchivo.add_command(label="Abrir")
archivoArchivo.add_command(label="Guardar")
archivoArchivo.add_command(label="Guardar como")
archivoArchivo.add_separator()
archivoArchivo.add_command(label="Cerrar", command=cerrarDocumento)
archivoArchivo.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoArchivo)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()