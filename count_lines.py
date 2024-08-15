# PUNTO 1
import os

path = 'w_names.txt'

if os.path.exists(path): # reviso si el archivo existe antes de leerlo
    with open(path, 'r') as file: # abro el archivo en modo lectura
        lines = file.readlines() # leo y guardo una lista con las lineas del archivo
    print("Hay " + str(len(lines)) + " lineas en el archivos")
else:
    print("El archivo " + path + " no existe")