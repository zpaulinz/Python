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
