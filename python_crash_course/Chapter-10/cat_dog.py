"""Reading files. Again."""
# Упражнения 10.8 и 10.9

files = ['cats.txt', 'nie', 'dogs.txt']

for file in files:
    try:
        with open(file) as f:
            result = f.read()
    except FileNotFoundError:
        pass
    else:
        print(result.strip())
