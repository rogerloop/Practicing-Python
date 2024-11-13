def suma(a,b):      #Nodificamos a y b en el scope de la suma
    a  = 3
    b  = 4
    return a + b

a, b = 5, 10
print(suma(a,b))  #Imprime 7
print(a, b)       #a y b no han cambiado fuera de la función

# ---------------------------------------

def minimo(l):
    l[0] = 1000  #Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print(l)

print(minimo(l[:]))   # Modifica la lista aquí

print(l)

#--------------- Sintaxis doble asterisco
def f(**Kargs):  # Azepta número de argumentos por nombre
    print(Kargs)

f()

f(a=1)

f(a=1, b=2)

f(a=1, c=3, b=2)