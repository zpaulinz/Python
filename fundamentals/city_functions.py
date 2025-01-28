def get_formatted_town_city(town, city, population=""):
    """Generates a neatly formatted town, country string."""
    if population:
        town_city = f"{town}, {city}, {population}"
    else:
        town_city = f"{town}, {city}"
    return town_city.title()
