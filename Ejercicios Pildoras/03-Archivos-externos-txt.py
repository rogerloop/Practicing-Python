from io import open

archivo_texto=open("/Users/rogerdefez/Documents/VSCWorkspace/Practicing-Python/Ejercicios Pildoras/pildoras.txt", "w")

frase="Me encanta practicar Python \n el miercoles"

frase2="\n También me gusta el martes y el jueves"

archivo_texto.write(frase)

archivo_texto=open("/Users/rogerdefez/Documents/VSCWorkspace/Practicing-Python/Ejercicios Pildoras/pildoras.txt", "r")

lineas_texto=archivo_texto.readlines()

archivo_texto.seek(11)

texto=archivo_texto.read()

archivo_texto.close()

print(lineas_texto)

print(texto)  # imprime desde la posición 11 hasta el final del archivo

archivo_texto=open("Ejercicios Pildoras/pildoras.txt", "a")

archivo_texto.write(frase2)

archivo_texto.close()  # No es necesario cerrar el archivo si se utiliza el contexto con

archivo_texto=open("Ejercicios Pildoras/pildoras.txt", "r")

print(archivo_texto.read())

archivo_texto.close()  # No es necesario cerrar el archivo si se utiliza el contexto con

archivo_texto=open("Ejercicios Pildoras/pildoras.txt", "r")

archivo_texto.seek((len(archivo_texto.read())/2)+1)

print(archivo_texto.read())  # imprime desde la mitad del archivo hasta el final

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())

archivo_texto.close()

archivo_texto=open("Ejercicios Pildoras/pildoras.txt", "r+") # abre el archivo en modo lectura y escritura

archivo_texto.seek(0)

archivo_texto.write("Comienzo de texto \n")

archivo_texto.seek(0)

print(archivo_texto.read())

archivo_texto.close()

archivo_texto=open("Ejercicios Pildoras/pildoras.txt", "r+") # abre el archivo en modo lectura y escritura

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta lista ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

# print(lista_texto)

print(archivo_texto.read())

archivo_texto.close()





 











