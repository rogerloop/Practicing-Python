""" Realiza una función que realice la descomposición en
factores de un número. Deberá devolver una lista con
los factores de dicho número. Recordad que la
descomposición en factores de un número consiste
en hallar el conjunto de números primos cuya
multiplicación dé dicho número como resultado."""

def factores_primos(numero):
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return factores



# Ejemplo de uso
numero = 12
print(f"Factores primos de {numero}: {factores_primos(numero)}")



