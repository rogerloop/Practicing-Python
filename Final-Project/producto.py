class Producto:

    # Construtor de la clase Producto i inicialización para los objetos producto
    # Construyo la clase Producto con atributos privados usando __xxxx  para conseguir un buen encapsulamiento
    # Con esta implementación evito accesos indeseados desde fuera de la clase

    def __init__ (self, nombre, categoria, precio, cantidad):

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0.")
    

        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Implementación de Getters para dar acceso controlado a los atributos de la clase cuando queremos coger datos
    
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria
    
    def get_precio(self):
        return self.__precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    # Implementamos los métodos con setters para guardar datos de manera controlada en los atributos de la clase.
    # Al mismo tiempo también doy validación a los datos para que cumplan con los requerimientos
   
    def set_precio(self, nuevo_precio):
        if  nuevo_precio > 0:
            self.__precio =  nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")
        
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual a 0")
        
    # Uso la función STR para la clase producto para que los objetos de la clase se representen en pantalla
    # mediante una cadena de texto maquetada cada vez que se les llame
    def __str__(self):
        return f"Nombre: {self.__nombre}, Categoria: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"
    
        