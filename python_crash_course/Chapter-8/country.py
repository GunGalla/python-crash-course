# Упражнение 8.6

def city_country(city, country):
    formatted_city = f'{city}, {country}.'
    return formatted_city


city = city_country('Moscow', 'Russia')
city_2 = city_country('Sofia', 'Bulgaria')
city_3 = city_country('Washington', 'USA')

print(city)
print(city_2)
print(city_3)
