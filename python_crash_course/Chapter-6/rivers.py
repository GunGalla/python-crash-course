# Упражнение 6.5

rivers = {
    'volga': 'russia',
    'nile': 'egypt',
    'thames': 'england'
    }

for river in rivers:
    print(f"The {river.title()} runs through {rivers[river].title()}!")

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())
