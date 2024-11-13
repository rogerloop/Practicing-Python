"""Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducidos"""

positivo = int(input("Introduce numeros positivos para sumarlos: "))
suma = 0
while positivo >= 0:
    suma = positivo + suma
    positivo = int(input("Introduce numeros positivos para sumarlos: "))
        
print ("La suma de los numeros positivos introducidos es: ", str(suma))

