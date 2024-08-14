# PUNTO 1

with open('w_names.txt', 'r') as file:
    lines = file.readlines()

print("Hay " + str(len(lines)) + " lineas en el archivos")