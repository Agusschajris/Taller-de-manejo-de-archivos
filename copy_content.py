# PUNTO 2

with open('w_names.txt', 'r') as file:
    content = file.read()

with open('empty.txt', 'w') as file:
    file.write(content)