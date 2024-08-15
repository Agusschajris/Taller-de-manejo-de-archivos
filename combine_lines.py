# PUNTO 3
import os

first_path = 'w_names.txt'
second_path = 'm_names.txt'

if os.path.exists(first_path): # reviso si el primer archivo existe antes de leerlo
    with open(first_path, 'r') as file: # abro el primer archivo en modo lectura
        w_lines = file.readlines() # leo y guardo una lista con las lineas del primer archivo
else:
    print("El archivo " + first_path + " no existe")

if os.path.exists(second_path): # reviso si el segundo archivo existe antes de leerlo
    with open(second_path, 'r') as file: # abro el segundo archivo en modo lectura
        m_lines = file.readlines() # leo y guardo una lista con las lineas del segundo archivo
    with open(second_path, 'w') as file: # abro el segundo archivo en modo escritura
        for i in range(len(m_lines)): # Itero a partir de la cantidad de líneas del segundo archivo
            file.write(m_lines[i].strip() + " " + w_lines[i]) # escribo cada linea de cada archivo concatenandolas (sacandoles el enter y el espacio)
else:
    print("El archivo " + second_path + " no existe")