# Defining a Function:
def greet_user(username):
    """Displays a simple greeting."""
    print(f"Hello {username.title()}!")
    
greet_user('amy')


# Arguments And Parameters:
def display_message():
    print("I am learning functions in this chapter.")
    
display_message()


# Positional Arguments:
def describe_pet(animal_type, pet_name):
    """Displays information about the pet."""
    print(f"\nMy pet is a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet('cat', 'tom')


# Arguments In The Form Of Keywords:
describe_pet(animal_type='hamster', pet_name='hagrid')
describe_pet(pet_name='hagrid', animal_type='hamster')
print()


# Default Values:
def describe_pet(pet_name, animal_type='dog'):
    """Displays information about the pet."""
    print(f"\nMy pet is a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='hagrid', animal_type='hamster')
print()

# Function Call Equivalents:
# Dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# Hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
print()


# Return Value:
def get_formatted_name(first_name, last_name):
    """Returns a neatly formatted full name."""
    full_name = f"{first_name} {last_name}" 
    return full_name.title() 

musician = get_formatted_name('jimi', 'hendrix') 
print(musician, 
      '\n')


# Defining An Argument As Optional:
def get_formatted_name(first_name, last_name, middle_name=''):
    """Returns a neatly formatted full name."""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)


# Dictionary Return:
def build_person(first_name, last_name, age=None):
    """Returns a dictionary with information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person 

musician = build_person('jimi', 'hendrix', age=27)
print(musician,
      '\n') 


# Using A Function Along With A While Loop:

def get_formatted_name(first_name, last_name):
    """Returns a neatly formatted full name."""
    full_name = f"{first_name} {last_name}" 
    return full_name.title() 

while True:
    print(f"\nPlease enter your first and last name:")
    print("(type 'q' to quit at any time)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name) 
    print(f"\nHello, {formatted_name}!")    
    

def get_city_country(city, country):
    """Returns a neatly formatted string of city and country."""
    return f"{city.title()}, {country.title()}"

print(get_city_country('warszawa', 'polska'))
print(get_city_country('hannover', 'niemcy'))


def make_album(artist, album_title, num_tracks=None):
    """Creates a dictionary representing a music album."""
    album_info = {'artist' : artist, 'album_title' : album_title}
    if num_tracks:
        album_info['num_tracks'] = num_tracks
    return album_info

albums = []

while True:
    print(f"\nPlease enter the information:")
    print("(type 'q' to quit at any time)")
    
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    
    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break
    
    num_tracks_input = input("Number of tracks (press Enter to skip): ")
    if num_tracks_input.lower() == 'q':
        break
        
    if num_tracks_input:
        num_tracks = int(num_tracks_input)
    else:
        num_tracks = None
        
    album = make_album(artist, album_title, num_tracks)
    albums.append(album)
    

print("\nAlbums you entered:")
for album in albums:
    print(album)
    
    
# Passing A List:
def greet_users(names):
    """Displays a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['amy', 'peter', 'sara']
greet_users(usernames)
print()

# Modifying A List In A Function:
unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all printed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print()


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each project until there are no more projects left
    in the list. 
    Each printed model is moved to the completed_models list.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Displays all models that have been printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print()
# Preventing A Function From Modifying A List:
# function_name(list_name[:]) # to pass a copy of a list

messages = ['yes', 'no', 'or', 'and']

def show_messages(messages):
    for message in messages:
        print (f"{message.title()}")
    
show_messages(messages[:])


messages = ['yes', 'no', 'or', 'and']
sent_messages = []

def send_messages(messages_copy, sent_messages):
    while messages_copy:
        message = messages_copy.pop(0)
        sent_messages.append(message)
        print (f"{message.title()}")
        
    
send_messages(messages[:], sent_messages)

print("\nOriginal messages list after sending:", messages)
print("Sent messages list:", sent_messages)


# Passing Any Number Of Arguments:
def make_pizza(*toppings):
    """Summarize the information about the pizza being prepared."""
    print("\nPreparing a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')


# Positional Arguments And Passing An Arbitrary Number Of Arguments:
def make_pizza(size, *toppings):
    """Summarize information about the pizza being prepared."""
    print(f"\nPreparing a {size} cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(40, 'pepperoni')
make_pizza(30, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Number Of Keyword Arguments:
# The **user_info parameter creates a dictionary to capture all 
# additional key-value arguments passed to the function.
def build_profile(first, last, **user_info):
    """Build a dictionary containing all user information."""
    user_info['first_name'] = first  
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
print()
# Parameter **kwargs, contains an arbitrary number of keyword arguments


def make_sandwich(*ingredients):
    print(f"\nPreparing a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"-{ingredient}")
    
make_sandwich('cheese', 'ham')
make_sandwich('cheese', 'ketchup')
make_sandwich('cheese', 'ham', 'butter', 'cucumber', 'salt')


def build_profile(first, last, **user_info):
    """Build a dictionary containing all user information."""
    user_info['first_name'] = first  
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('amy', 'black',
                             location='usa',
                             field='biology')
print(user_profile)


def make_car(brand, model, **car_info):
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)