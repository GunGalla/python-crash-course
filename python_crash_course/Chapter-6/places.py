# Упражнение 6.9, 6.10

favorite_places = {
    'Kirill': ['Red Square', 'Thames', 'New-York'],
    'Volodya': ['London'],
    'Yaroslav': ['Saransk', 'Los Angeles']
    }

for person, place in favorite_places.items():
    if len(place) == 1:
        print(f"{person}'s favorite place is {place[0]}!")
    else:
        print(f"{person}'s favorite places are:")
        for cur_place in place:
            print(f"\t{cur_place}")
