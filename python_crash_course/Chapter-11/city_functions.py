"""Build formatted city name."""
# Упражнения 11.1 и 11.2


def formatted_city(city, country, population=''):
    if population:
        formatted_name = f"{city}, {country} - population {population}"
        return formatted_name.title()
    else:
        formatted_name = f"{city}, {country}"
        return formatted_name.title()
