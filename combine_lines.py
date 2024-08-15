with open('w_names.txt', 'r') as file:
    w_lines = file.readlines()

with open('m_names.txt', 'r') as file:
    m_lines = file.readlines()

with open('m_names.txt', 'w') as file:
    for i in range(len(m_lines)):
        file.write(m_lines[i].strip() + " " + w_lines[i])