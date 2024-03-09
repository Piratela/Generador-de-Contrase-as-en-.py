import random
import string

def generar_contrasena(num_mayusculas, num_minusculas, num_numeros, num_simbolos):
    # Caracteres posibles para cada tipo
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Lista que contendrá todos los caracteres posibles
    caracteres = []

    # Agregar caracteres a la lista según la cantidad especificada
    caracteres.extend(random.sample(mayusculas, num_mayusculas))
    caracteres.extend(random.sample(minusculas, num_minusculas))
    caracteres.extend(random.sample(numeros, num_numeros))
    caracteres.extend(random.sample(simbolos, num_simbolos))

    # Mezclar la lista para que los caracteres estén en orden aleatorio
    random.shuffle(caracteres)

    # Convertir la lista a una cadena para obtener la contraseña final
    contrasena = ''.join(caracteres)
    return contrasena

# Solicitar al usuario la cantidad de caracteres de cada tipo
num_mayusculas = int(input("Número de mayúsculas: "))
num_minusculas = int(input("Número de minúsculas: "))
num_numeros = int(input("Número de números: "))
num_simbolos = int(input("Número de símbolos: "))

# Generar y mostrar la contraseña
contrasena_generada = generar_contrasena(num_mayusculas, num_minusculas, num_numeros, num_simbolos)
print("Contraseña generada:")
print(contrasena_generada)
