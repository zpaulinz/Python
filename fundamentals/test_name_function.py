from name_function import get_formatted_name

def test_first_last_name(self):
    """Are the data in the form 'Janis Joplin' handled correctly?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name(self):
    """Are the data in the form 'Wolfgang Amadeus Mozart' handled correctly?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'