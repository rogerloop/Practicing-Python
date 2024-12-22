# 1. Dados dos números, escriba un código Python para encontrar //
# el mínimo de estos dos números

def minimum(a, b):

    if a <= b:
        return a
    else:
        return b
    
a = -1
b = -4
print(minimum(a, b))


# 2. Invertir palabras de una cadena dada.

Str = 'código de práctica de prueba geeks'

def rev_sentence(sentence):
    # dividir la frase en palabras
    words = sentence.split(' ')
    # invertir cada palabra
    reverse_sentence = ' '.join(reversed(words))

    return reverse_sentence

if __name__ == "__main__":
    input = Str
    print (rev_sentence(input))


# 3. Realizar una suma de los elementos de una tupla

test_tup = (7, 8, 9, 1, 10, 7)

print( "la tupla original es : " + str(test_tup))

res = sum(list(test_tup))
print("la suma de los elementos de la tupla es : " + str(res))


# 4. Escriba un código que calcule una lista de números proporcionados.

def list_sum(num_List):
    if len(num_List) == 0:
         
         return 0
    else:
         return num_List[0] + list_sum(num_List[1:])
    
    
print(list_sum([5, 6, 10, 8, 4]))
   
# 5. Escriba un código que desordene al azar una lista.

from random import shuffle
x = ['Skyrim', 'Pertenece', 'A', 'Los', 'Nordicos']
shuffle(x)
print(x)

# 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

# Definir el nombre del archivo a examinar
archivo = "07-Test-practico.py"  

with open(archivo) as fh:
    text = fh.read()

# Dividir el texto en palabras
palabras = text.split()

count = 0
for palabra in palabras:
    if palabra.isupper():
        count += 1

print("Total de palabras en mayúsculas:", count)

# Ejemplo Bucle

for i in [1, 10]:
    print("Hola")


