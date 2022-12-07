# Упражнение 6.11

cities = {
    'London': {
        'country': 'Great Britain',
        'population': 10000000,
        'fact': 'the capital',
        },
    'Moscow': {
        'country': 'Russia',
        'population': 12000000,
        'fact': 'good city',
        },
    'Sofia': {
        'country': 'Bulgaria',
        'population': 1000000,
        'fact': 'great place to live',
        },
    }

for city, city_info in cities.items():
    print(f"I like {city}!\nThis city is in {city_info['country']}.\nThere are"
          f" {city_info['population']} people live here."
          f"\nThe funniest fact that it is a {city_info['fact']}!")
