from tkinter import *

class Calculadora:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora OOP")

        self.operacion = ""
        self.resultado_parcial = 0.0
        self.numero_registro = ""
        self.reset_pantalla = False
        self.resultado_total = 0.0

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la interfaz gráfica con Tkinter."""
        self.frame = Frame(self.ventana, padx=10, pady=10)
        self.frame.pack()

        self.numero_pantalla = StringVar()
        self.registro_pantalla = StringVar()

        # Pantalla superior para registro
        self.pantalla_registro = Entry(self.frame, textvariable=self.registro_pantalla, state='readonly', background="black", fg="#03f943", justify="right")
        self.pantalla_registro.grid(row=0, column=0, padx=10, pady=5, columnspan=4)
        self.registro_pantalla.set("")  # Inicializa con vacío

        # Pantalla inferior para resultado
        self.pantalla = Entry(self.frame, textvariable=self.numero_pantalla, background="black", fg="#03f943", justify="right")
        self.pantalla.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
        self.numero_pantalla.set("0")  # Inicializa con 0

        self.crear_botones()

    def crear_botones(self):
        """Crea los botones de la calculadora."""
        botones = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3, self.division),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3, self.multiplicacion),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3, self.resta),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, self.resultado), ("+", 5, 3, self.suma),
            ("AC", 6, 0, self.borrar_ultimo), ("C", 6, 1, self.borrar_todo)
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
        self.numero_registro += num + " " + operacion + " "
        self.operacion = operacion
        self.reset_pantalla = True
        self.registro_pantalla.set(self.numero_registro)

    def suma(self):
        self.operacion_matematica(self.numero_pantalla.get(), " + ")

    def resta(self):
        self.operacion_matematica(self.numero_pantalla.get(), " - ")

    def multiplicacion(self):
        self.operacion_matematica(self.numero_pantalla.get(), " * ")

    def division(self):
        self.operacion_matematica(self.numero_pantalla.get(), " / ")

    def resultado(self):
        """Calcula el resultado final de la operación."""
        if self.operacion and self.numero_pantalla.get():
            try:
                num_actual = float(self.numero_pantalla.get())
                if self.operacion == " + ":
                    self.resultado_parcial += num_actual
                elif self.operacion == " - ":
                    self.resultado_parcial -= num_actual
                elif self.operacion == " * ":
                    self.resultado_parcial *= num_actual
                elif self.operacion == " / ":
                    if num_actual != 0:
                        self.resultado_parcial /= num_actual
                    else:
                        self.numero_pantalla.set("Error")
                        return

                self.numero_pantalla.set(str(self.resultado_parcial))
                self.resultado_total = self.resultado_parcial
                self.numero_registro = str(self.resultado_parcial)  # Reinicia el registro
                self.registro_pantalla.set(self.numero_registro)
                self.operacion = ""
            except ValueError:
                self.numero_pantalla.set("Error")

    def borrar_ultimo(self):
        """Borra el último número u operador ingresado."""
        if self.numero_pantalla.get() != "0":
            self.numero_pantalla.set(self.numero_pantalla.get()[:-1])
        else:
            self.numero_registro = self.numero_registro.strip().rsplit(" ", 1)[0]  # Elimina el último operador o número
            self.registro_pantalla.set(self.numero_registro)

    def borrar_todo(self):
        """Borra todo el historial, los resultados y los valores en pantalla."""
        self.numero_pantalla.set("0")
        self.registro_pantalla.set("")
        self.numero_registro = ""
        self.operacion = ""
        self.resultado_parcial = 0.0
        self.resultado_total = 0.0

    def iniciar(self):
        """Inicia el loop principal de Tkinter."""
        self.ventana.mainloop()


# Instancia y ejecución de la calculadora
if __name__ == "__main__":
    app = Calculadora()
    app.iniciar()
