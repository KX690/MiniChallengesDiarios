import random
import string

longitud= random.randint(8,16)
i=0
contrasenia=""
for _ in range (longitud):
    i+=1
    match i:
        case 1:
            contrasenia+=random.choice(string.ascii_letters)
        case 2:
            contrasenia+=random.choice(string.ascii_lowercase)
        case 3:
            contrasenia+=random.choice(string.ascii_uppercase)
        case 4:
            contrasenia+=random.choice(string.digits)
            i=0
print(f"La contraseña generada es: {contrasenia}\nLongitudo {longitud}")