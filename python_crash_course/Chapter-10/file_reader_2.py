"""Reads file in a different ways."""
# Упражнение 10.1

with open('learning_python.txt') as file:
    contents = file.read()

print(contents)

with open('learning_python.txt') as file:
    content_list = file.readlines()
    for line in content_list:
        print(f'\n{line.strip()}')

print(content_list)

# Упражнение 10.2

with open('learning_python.txt') as file:
    content_list = file.readlines()
    for line in content_list:
        print(f"\n{line.replace('Python', 'C').strip()}")
