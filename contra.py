import random
import string

def generar_password(n):
    s = ""
    caracteres = list(string.printable)
    caracteres = caracteres[:-6]
    for i in range(n):
        s += random.choice(caracteres)
    print(s)
    m = len(caracteres)
    p = (1/len(caracteres))**n
    print("La probabilidad de que descubran su contraseña es {:.2e}".format(p))
