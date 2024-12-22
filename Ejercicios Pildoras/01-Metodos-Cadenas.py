email = ""
arroba = 0

while (arroba!=1 or email.rfind('@') == (len(email)-1) or email.find('@') == 0):

    email = input ("Introduce tu eMail: ")

    arroba = email.count("@")

    print("El correo electrónico no es válido")

else:
    print("El correo electrónico es válido")
