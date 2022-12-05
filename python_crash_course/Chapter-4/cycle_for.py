# Упражнение 4.3
for num in range(1, 21):
    print(num)

# Упражнения 4.4 и 4.5
items = list(range(1, 1000001))
print(items)
print(min(items))
print(max(items))
print(sum(items))

# Упражнение  4.6
not_even_nums = []
for num in range(1, 21, 2):
    not_even_nums.append(num)

print(not_even_nums)

# Упражнение 4.7
even_3 = []
for num in range(3, 31):
    if num % 3 == 0:
        even_3.append(num)

print(even_3)

items = list(range(3, 31, 3))
print(items)

# Упражнение 4.8
qubes = []
for num in range(1, 11):
    qubes.append(num ** 3)

print(qubes)

# Упражнение 4.9
qubes = [x ** 3 for x in range(1, 11)]
print(qubes)
