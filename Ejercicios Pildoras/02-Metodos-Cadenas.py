# ejemplo uso metodo de cadenas (isdigit) Pildoras!!

edad=input("introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numérico")

    edad = input ("Introduce la edad :")
    
if (int(edad)<18):
    print("No puede pasar")

else:
    print("Puedes pasar")

