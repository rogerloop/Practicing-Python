
milista  = [1 ,2 ,3 ,4 ,5 ,6 ,7 ]
print(milista)

## milista2 tiene los valores (2*elemento) siendo elemento los valores de la Lista milista
milista2 = [2*elemento for elemento in milista]
print(milista2)

##Crear una Lista solo con los elementos pares
listaPares = [elemento for elemento in milista if elemento%2==0]
print(listaPares)

##A La manera tradicional seria: listaPares=[]
for i in milista:
    if i%2==0:
        listaPares.append (i)
print(listaPares)

##Anidar iteraciones dentro de la Liata 
a=["a", "b", "c"]
b=[1,2,3]

##Para cada elemento de a me recorre todos los elmentos de b 
c = [elemento1*elemento2 for elemento1 in a for elemento2 in b]
print (c)

##Puedo incluso poner alguna condicion
c = [elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(c)