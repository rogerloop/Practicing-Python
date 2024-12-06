""" Mediante este archivo y metodos crearé un menú para terminal que permita seleccionar 
las diferentes opciones solicitadas en el enunciado
"""
# Importo las clases definidas en los módulos auxiliares.

from inventario import Inventario
from producto import Producto

# defino la función principal "main" que permitirá desarrollar el menú mediante condicionales y un bucle infinito while

def main():

    # Creo objeto inventario que me permite realizar las operaciones(metodos) de la clase inventario
    
    inventario = Inventario()

    # Creo un buncle infinito con While True para mantener el menú activo lo muestro en terminal mediante print y capturo el imput de usuario

    while True:
        print ("\n ** Menu de opciones sobre inventario **\n")
        print("1. Agrega un producto")
        print("2. Actualizar un producto")
        print("3. Elimina un producto")
        print("4. Muestra el inventario")
        print("5. Busca un producto")
        print("6. Salir")

        """En la siguiente linea capturo la "opción" deseada por el usuario y en función de la misma actuará una sección del
        código u otra, mediante las condiciones if, elif.
        Uso try except para control de errores en todas las secciones y evitar entradas no deseadas"""

        try:
            opcion = int(input("\nSelecciona una de las opciones: "))
        except ValueError:
            print("Opción no valida, por favor teclea un número del 1 al 6.")
            continue

            
        if opcion == 1:     #Agrega un producto
            
            """Creo un bucle While y uso función .strip para validar y asegurarme 
            que ni nombre ni categoría queden vacios."""
           
            while True:
                nombre = input("\nIntroduce un nombre para el producto: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
                    continue
                categoria = input("Ingresa una categoría para este producto: ").strip()
                if not categoria:
                    print("La categoría no puede estar vacía. Por favor, repite.")
                    continue
 
                try:
                    # VAlidación de precio y cantidad también con la ayuda de  los setters de la clase Producto implementados en "producto.py"

                    precio = float(input("Precio del producto: "))
                    cantidad = int(input("Cantidad de producto: "))
                    new_producto = Producto (nombre, categoria, precio, cantidad)
                    inventario.agregar_producto(new_producto)
                    break   # Aquí cierro el bucle while después de agregar y paso a tratar excepciones
               
                except ValueError:
                    print("Valor no valido, por favor, introduce de nuevo, \nrecuerda: Precio debe ser mayor que 0 (x.xx) - cantidad debe ser nº entero mayor o igual a 0")
                    continue


        elif opcion == 2:       #Actualizar un producto

            """Con esta opción activo  el método actualizar producto del módulo inventario.
            Aquí usamos "try" para evitar interrupciones y contolar posibles errores
             en la intoducción de precios y cantidades a actualizar."""
            
            nombre = input("Introduce el nombre del producto que quieres actualizar: ")
            try:
                nuevo_precio = input("Nuevo precio (deje vacío para no cambiar): ")
                nueva_cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
               
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad  else None

                # Valido los inputs antes de actualizar

                if nuevo_precio is not None and nuevo_precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0.")
                if nueva_cantidad is not None and nueva_cantidad < 0:
                    raise ValueError("La cantidad debe ser mayor o igual a 0.")

                inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)

            except ValueError as e:
                print(f"Error: {e} Datos inválidos. \nrecuerda: Precio debe ser mayor que 0 (x.xx) - cantidad debe ser nº entero mayor o igual a 0")
         

        elif opcion == 3:       #Elimina un producto

            """Pido mediante input el nombre de producto a eliminar y paso el nombre al 
            método de la clase Inventario en "inventario.py" para que proceda"""
        
            nombre = input("Introduce el nombre del producto que quieres eliminar: ")
            inventario.eliminar_producto(nombre)


        elif opcion == 4:       #Muestra el inventario

            # Muy sencillo simplemente se hace una llamada al método de "inventario.py" para que proceda

            inventario.mostrar_inventario()        

        
        elif opcion == 5:       #Busca un producto
            
            """Pasamos el nombre del producto a buscar mediante argumento, al método del módulo
            "inventario.py" correspondiente (buscar_product)"""

            nombre = input("Introduce el nombre del producto que quieresa buscar: ")
            inventario.buscar_producto(nombre)


        # Preparo una salida del programa elegante con opción de cancelación.
        # Uso función upper para discriminar mayuscukas y minusculas 

        elif opcion == 6:           
            while True:
                salir = (input("Salir de la aplicación de inventario, ¿estas seguro? S/N: ")).upper()
                if salir == "S":
                    print("Muchas gracias por usar Inventario")
                    exit()
                elif salir == "N":
                    break
                else:
                    print("Recuerda debes seleccionar S o N")

        else:
             print("Opción no válida. Intente de nuevo.")

"""Con la linea final de código aseguramos que la función "main()" solo se ejecuta desde dentro de este archivo
es un convencionalismo que permite asegurar la lógica del programa, reutilización de código etc.
En nuestro caso al tener 3 módulos define claramente cual es el archivo principal y solo en caso de que ejecutemos "main.py"
toda la solución funcionará.
"""

if __name__ == "__main__":
    main()



    



