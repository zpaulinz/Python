from city_functions import get_formatted_town_city 

def test_get_formatted_town_city():
    # Test 1: Standard case
    result = get_formatted_town_city('Santiago', 'Chile')
    assert result == 'Santiago, Chile'
    
    # Test 2: Town and country with one word
    result = get_formatted_town_city('Warsaw', 'Poland')
    assert result == 'Warsaw, Poland'
    
    # Test 3: Town and country with multiple words
    result = get_formatted_town_city('New York', 'United States')
    assert result == 'New York, United States'
    
    # Test 4: Check proper capitalization
    result = get_formatted_town_city('paris', 'france')
    assert result == 'Paris, France'
    
    
def test_get_formatted_town_city_population():
    # Test 1: Town, country, and population
    result = get_formatted_town_city('Santiago', 'Chile', '5000000')
    assert result == 'Santiago, Chile, 5000000'
    
    # Test 2: Town, country, and population with multiple words
    result = get_formatted_town_city('New York', 'United States', '8500000')
    assert result == 'New York, United States, 8500000'
    
    # Test 3: Check population with a space
    result = get_formatted_town_city('Tokyo', 'Japan', '9 000 000')
    assert result == 'Tokyo, Japan, 9 000 000'
    
    # Test 4: Town and country with empty population
    result = get_formatted_town_city('London', 'England', '')
    assert result == 'London, England'
