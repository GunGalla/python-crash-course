# Упражнение 8.12

def sandwich(*args):
    return list(args)


print(sandwich('pepperoni', 'melt'))
print(sandwich('bacon', 'butter', 'cheese'))
print(sandwich('nothing'))
