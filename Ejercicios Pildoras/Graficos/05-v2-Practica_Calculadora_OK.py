from tkinter import *

raiz=Tk()

miFrame = Frame(raiz, padx=10, pady=10)
miFrame.pack()

operacion = ""
resultadoParcial = None  # Ahora comienza como None para evitar cálculos incorrectos
reset_pantalla = False

#----------Pantalla------------------

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
numeroPantalla.set("0")

#-------Pulsaciones Teclado-------------

def numeroPulsado(num):
    global reset_pantalla

    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:    
        # Evitar doble punto decimal
        if num == "." and "." in numeroPantalla.get():
            return
        numeroPantalla.set(numeroPantalla.get() + num)

#----------Funciones Aritméticas------------------

def operar(tipo):
    global operacion, resultadoParcial, reset_pantalla

    try:
        num = float(numeroPantalla.get())
    except ValueError:
        return

    if resultadoParcial is None:
        resultadoParcial = num
    else:
        calcular()

    operacion = tipo
    reset_pantalla = True

def calcular():
    global operacion, resultadoParcial

    try:
        num = float(numeroPantalla.get())
    except ValueError:
        return

    if resultadoParcial is None:
        return

    if operacion == "suma":
        resultadoParcial += num
    elif operacion == "resta":
        resultadoParcial -= num
    elif operacion == "multiplicacion":
        resultadoParcial *= num
    elif operacion == "division":
        if num != 0:
            resultadoParcial /= num
        else:
            numeroPantalla.set("Error")
            resultadoParcial = None
            return

    numeroPantalla.set(str(resultadoParcial))
    operacion = ""

#-----------Fila 1-----------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:operar("division"))
botonDiv.grid(row=2, column=4)

#-----------Fila 2-----------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="*", width=3, command=lambda:operar("multiplicacion"))
botonMult.grid(row=3, column=4)

#-----------Fila 3-----------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:operar("resta"))
botonRest.grid(row=4, column=4)

#-----------Fila 4-----------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:calcular())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:operar("suma"))
botonSum.grid(row=5, column=4)

raiz.mainloop()
