T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzaca el nuevo elemento: ")))
T = tuple(L)
print("Tupla final")
print(T)

#---------------

# Declaramos variables
a = 20
b = 10

# Suma
sum = a+b

# Resta 
sub = a-b

# Salida
print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))

