from tkinter import *

raiz = Tk()

myFrame=Frame(raiz, width=1200, height=600)
myFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(myFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

nombreLabel=Label(myFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cuadroPass=Entry(myFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

passLabel=Label(myFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroApellido=Entry(myFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

apellidoLabel=Label(myFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion=Entry(myFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

direccionLabel=Label(myFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

textoComentario=Text(myFrame, width=25, height=5)
textoComentario.grid(row=4, column=1, sticky="w", padx=10, pady=10)

scrollVert=Scrollbar(myFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

comentariosLabel=Label(myFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()