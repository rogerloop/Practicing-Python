class Inventario:
    # Construyo clase y creo lista vacia para almacenar los productos del inventario
    
    def __init__(self):
        self.__productos = []

    # Creación de metodos (funciones) para manejar los inputs del usuario

    """Agregando productos con appeand y control si ya existe para evitar duplicados mediante el if / else.
    Recojo el objeto de la clase producto definido con sus variables en el constructor de "producto.py" lleno este objeto con los 
    datos recogidos mendiante inputs enla opción 1 de "main.py" . Finalmente traslado el objeto producto con sus variables aquí. 
    Hago una comprobación por comparación de nombre "if any" por si hay algun nombre igual al que trae el objeto producto. Si encuentra un nombre igual no crea producto y 
    avisa que ya existe, en caso contrario, o sea no encuetra nombre en la lista "self.__productos", añado mediante "append" el objeto producto
    con sus atributos a la lista """

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
                print(f"El producto '{producto.get_nombre()}' ya existe en el inventario. Si desea actualizar precio o cantidad elija opción '2'.")
        else:
            self.__productos.append(producto)
            print ("Producto añadido de forma correcta")
       
    """ Mediante este método tenemos la posibilidadde actualizar los productos. En la primera parte de la condición.
    comprobamos que el producto exista, si existe, actualizo precio y/o cantidad, con comprobación en el módulo producto.py
    que los dartos de precio y/o cantidad sean validos."""

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

    """ Metodo para eliminar productos del inventario, recojo la variable "nombre" de la opción 3 (eliminar producto) 
    del modulo main.py y lo paso como argumento recorro la lista almacenada en self.__productos con bucle "for" y comparo 
    con if cada nombre de la lista con el nombre pasado por argumento. En cuanto encuentro la coincidencia elimino todo el 
    objeto producto con remove y acabo el metodo con return. Caso de no encontrar imprimo mensaje de no encontrado"""
    
    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                print(f"\nSe ha eliminado '{nombre}' del inventario de manera satidfactoria.")
                return
        print(f"\nEl producto '{nombre}' no se encontró en el inventario. \nCon la opcion '4' del menu veraas un listado de productos disponibles")

    """ Este método lo activo con la opción 4 del menú de "main.py" Es muy sencillo ya que lo unico que hace es recorrer la lista self.__productos 
    que creamos en este mismo modulo imprimiendo todos los objetos de la clase "producto" que he ido almacenando en la lista"""
    
    def mostrar_inventario(self):
        for producto in self.__productos:
            print(f"El Inventario de productos es: {producto}")

    """ Para este método buscar que corresponde a la opción 5 del módulo "main.py", es muy fácil sigo el mismo patron 
    que el método "eliminar" o incluso "actualizar_producto". Aquí es más sencillo porque la única acción despues de la comparación es mostrar
    el producto encontrado o caso contrario "print" no encontrado """

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                return
        print(f"El producto '{nombre}' no se encontró en el inventario.")






            




            
