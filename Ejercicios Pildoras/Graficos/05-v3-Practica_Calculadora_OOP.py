from tkinter import *

class Calculadora:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora OOP")

        self.operacion = ""
        self.resultado_parcial = 0.0
        self.reset_pantalla = False

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la interfaz gráfica con Tkinter."""
        self.frame = Frame(self.ventana, padx=10, pady=10)
        self.frame.pack()

        self.numero_pantalla = StringVar()
        self.pantalla = Entry(self.frame, textvariable=self.numero_pantalla, background="black", fg="#03f943", justify="right")
        self.pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        self.numero_pantalla.set("")

        self.crear_botones()

    def crear_botones(self):
        """Crea los botones de la calculadora."""
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3, self.division),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3, self.multiplicacion),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3, self.resta),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2, self.resultado), ("+", 4, 3, self.suma)
        ]

        for btn in botones:
            texto, fila, columna = btn[:3]
            comando = btn[3] if len(btn) > 3 else lambda t=texto: self.numero_pulsado(t)
            Button(self.frame, text=texto, width=5, command=comando).grid(row=fila, column=columna, padx=5, pady=5)

    def numero_pulsado(self, num):
        """Maneja la entrada de números en la calculadora."""
        if self.reset_pantalla:
            self.numero_pantalla.set(num)
            self.reset_pantalla = False
        else:
            if num == "." and "." in self.numero_pantalla.get():
                return
            self.numero_pantalla.set(self.numero_pantalla.get() + num)

    def operacion_matematica(self, num, operacion):
        """Ejecuta una operación matemática."""
        if self.operacion:
            self.resultado()
        self.resultado_parcial = float(num)
        self.operacion = operacion
        self.reset_pantalla = True

    def suma(self):
        self.operacion_matematica(self.numero_pantalla.get(), "suma")

    def resta(self):
        self.operacion_matematica(self.numero_pantalla.get(), "resta")

    def multiplicacion(self):
        self.operacion_matematica(self.numero_pantalla.get(), "multiplicacion")

    def division(self):
        self.operacion_matematica(self.numero_pantalla.get(), "division")

    def resultado(self):
        """Calcula el resultado final de la operación."""
        if self.operacion and self.numero_pantalla.get():
            try:
                num_actual = float(self.numero_pantalla.get())
                if self.operacion == "suma":
                    self.resultado_parcial += num_actual
                elif self.operacion == "resta":
                    self.resultado_parcial -= num_actual
                elif self.operacion == "multiplicacion":
                    self.resultado_parcial *= num_actual
                elif self.operacion == "division":
                    if num_actual != 0:
                        self.resultado_parcial /= num_actual
                    else:
                        self.numero_pantalla.set("Error")
                        return
                
                self.numero_pantalla.set(str(self.resultado_parcial))
                self.operacion = ""
            except ValueError:
                self.numero_pantalla.set("Error")

    def iniciar(self):
        """Inicia el loop principal de Tkinter."""
        self.ventana.mainloop()


# Instancia y ejecución de la calculadora
if __name__ == "__main__":
    app = Calculadora()
    app.iniciar()
