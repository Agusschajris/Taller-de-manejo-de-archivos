# PUNTO 2
import os

path = 'w_names.txt'

if os.path.exists(path): # reviso si el archivo existe antes de leerlo
    with open(path, 'r') as file: # abro el archivo en modo lectura
        content = file.read() # leo y guardo el contenido del archivo
    with open('empty.txt', 'w') as file: # creo un archivo vacío y lo abro en modo escritura
        file.write(content) # escribo en el nuevo archivo el contenido del archivo anterior
else:
    print("El archivo " + path + " no existe")