"""Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior."""

numero = int(input("Introduce cada vez un número mayor que el anterior: "))
anterior = numero
while True:
    nuevo = int(input("Introduce un número mayor que el anterior: "))
    if nuevo <= anterior:
        print(f"Has perdido el juego al introducir el número {nuevo} que es menor o igual que el anterior {anterior}")  # No se imprime
        break

    anterior = nuevo
    

        