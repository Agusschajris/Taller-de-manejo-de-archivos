with open('w_names.txt', 'r') as file:
    w_lines = file.readlines()

with open('m_names.txt', 'r') as file:
    m_lines = file.readlines()

with open('m_names.txt', 'w') as file:
    for m_line, w_line in zip(m_lines, w_lines):
        file.write(m_line.strip() + " " + w_line)