from tkinter import *
from turtle import right

raiz=Tk()

raiz.title("Ventana de pruebas")

# raiz.resizable(True,False)

raiz.geometry("650x350")

raiz.config(bg="blue")

raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame=Frame()

#miFrame.pack(side="right", anchor="n")

#miFrame.pack(fill="y", expand="True")

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

raiz.mainloop()

