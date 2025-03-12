from tkinter import *

root=Tk()

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
archivoArchivo.add_command(label="Cerrar")
archivoArchivo.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoArchivo)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()