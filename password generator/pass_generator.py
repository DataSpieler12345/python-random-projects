import string
import random

def pass_generator(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    return password

longitud = int(input("enter the length of your password: "))

# Llamada a la función para generar una contraseña de longitud 12
# contrasena = pass_generator(10)
# print(contrasena)

new_password = pass_generator(longitud)
print("your password is: ", new_password)