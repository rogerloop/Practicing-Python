class Inventario:
    # Construyo clase y creo lista vacia para almacenar los productos del inventario
    
    def __init__(self):
        self.__productos = []

    # Creación de metodos (funciones) para manejar los inputs del usuario

    # Agregando productos con appeand y control si ya existe para evitar duplicados mediante el if / else

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
                print(f"El producto '{producto.get_nombre()}' ya existe en el inventario. Si desea actualizar precio o cantidad elija opción '2'.")
        else:
            self.__productos.append(producto)
            print ("Producto añadido de forma correcta")
       
    # Mediante este método tenemos la posibilidadde actualizar los productos. En la primera parte de la condición.
    # comprobamos que el producto exista, si existe, actualizo precio y/o cantidad, con comprobación en el módulo producto.py
    # que los dartos de precio y/o cantidad sean validos.

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
            else:
                print(f"El producto '{nombre}' no se encontró en el inventario. \nSi desea crear un nuevo producto elija opción '1'.")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                print(f"\nSe ha eliminado '{nombre}' del inventario de manera satidfactoria.")
                return
        print(f"\nEl producto '{nombre}' no se encontró en el inventario. \nCon la opcion '4' del menu veraas un listado de productos disponibles")

    def mostrar_inventario(self):
        for producto in self.__productos:
            print(f"El Inventario de productos es: {producto}")


    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                return
        print(f"El producto '{nombre}' no se encontró en el inventario.")






            




            
