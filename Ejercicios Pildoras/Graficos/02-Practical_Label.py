from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

#miLabel= Label(miFrame, text="Hola alumnos de Python")
#miLabel.place(x=100, y=200)

Label(miFrame, text="Hola alumnos de Python", bg="red", fg="white", 
      font=("Comic Sans MS", 18)).place(x=100, y=100)

miImagen=PhotoImage(file="Ejercicios Pildoras/Graficos/avatar.gif")

Label(miFrame, image=miImagen).place(x=200, y=200)

root.mainloop()
