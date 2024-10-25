print("")
print("Alvaro Campechano 3W")
print(" ")


# Ejemplo de uso de la función open() para leer un archivo

# Instrucciones
print("Para abrir el archivo, utilice la función incorporada open().")
print("La open() función devuelve un objeto de archivo, que tiene un método read() para leer el contenido del archivo:")

# Crear un archivo de ejemplo
nombre_archivo = "demofile.txt"
contenido_archivo = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

# Escribir el contenido en demofile.txt
with open(nombre_archivo, 'w') as f:
    f.write(contenido_archivo)

# Leer el archivo y mostrar su contenido
try:
    f = open(nombre_archivo, "r")
    print("\nContenido del archivo:")
    print(f.read())
    f.close()  # No olvides cerrar el archivo después de usarlo
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
