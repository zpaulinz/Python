# Dictionaries Examples:
# key : value
alien_0 = {'color' : 'green',
           'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You have earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting With an Empty Dictionary:
alien_0 = {}

alien_0['color'] = 'zielony'
alien_0['points'] = 5
print(alien_0)


# Modifying Dictionary Values:
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


alien_0 = {'x_position': 0,
           'y_position': 25,
           'speed': 'medium'}

print(f"Initial x-position value: {alien_0['x_position']}")
# Moving the alien to the right.
# Determining the distance the alien should move based on its speed.
if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # It must be a fast alien.
    x_increment = 3


# The new position is the current position plus x_increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position value: {alien_0['x_position']}")


# Removing A Key-Value Pair:
alien_0 = {'color': 'zielony', 'points': 5}
print(alien_0)

del alien_0['points'] 
print(alien_0,
      '\n')
# Note that removing a key-value pair is irreversible!


# Dictionary of Similar Objects:
favorite_languages = {
    'john': 'python',
    'amy': 'c',
    'edward': 'rust',
    'paul': 'python',
}

language = favorite_languages['amy'].title()
print(f"Amy's favorite programming language is {language}.\n")


# Using The Get() Method To Access Values:
# get() requires a key and an optional default
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No points assigned.')
print(point_value,
      '\n')
# Use get() if the key might not exist in the dictionary.

person = {'name' : 'Amy',
          'lastname' : 'Blue',
          'age' : '20',
          'city' : 'New York'}
print(person,
      '\n')

fav_numbers = {'Amy' : 5,
               'Paul' : 7,
               'Edward' : 3}

print(fav_numbers,
      '\n')


# Iterating Through A Dictionary:
# You can iterate through all key-value pairs, or just keys or values.

# Iterating Through All Key-Value Pairs:
# This loop works for dictionaries with a million entries.
user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski',
}
print(user_0.items())

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
print()
    
favorite_languages = {
    'john': 'python',
    'amy': 'c',
    'edward': 'rust',
    'paul': 'python',
}

for name, language in favorite_languages.items():
    print(
    f"The favorite programming language of user {name.title()} is "
    f"{language.title()}.\n")


# Iterating Through All Dictionary Keys:
favorite_languages = {
    'john': 'python',
    'amy': 'c',
    'edward': 'rust',
    'paul': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
    # Equivalent to:
for name in favorite_languages:
    print(name.title())

print()

favorite_languages = {
    'john': 'python',
    'amy': 'c',
    'edward': 'rust',
    'paul': 'python',
}

friends = ['amy', 'john']

for name in favorite_languages.keys():
    print(f"Hello, {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tHello, {name.title()}! Your favorite programming "
              f"language is {language}!")

if 'peter' not in favorite_languages.keys():
    print("Peter, please take part in our survey!")

print()


# Iterating Through Ordered Dictionary Keys:
# Dictionary iteration follows insertion order, but can be modified
favorite_languages = {
    'john': 'python',
    'amy': 'c',
    'edward': 'rust',
    'paul': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for participating in the survey.")
print()


# Iterating Through All Dictionary Values:
print(f"The following programming languages were mentioned "
      f"in the survey:")
for language in favorite_languages.values():
    print(language.title())
    
# This approach gets all values, but a set shows only unique ones.
print(f"The following programming languages were mentioned "
      f"in the survey:")
for language in set(favorite_languages.values()):
    print(language.title())

print()


#Set Example:
languages = {'python', 'rust', 'python', 'c'}
print(languages,
      '\n')


# Nesting:
# List of Dictionaries:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
    print(alien)
    
print()

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


# List in a Dictionary:
# Storing information about the pizza ordered by the customer.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Order summary.
print(f"You've ordered a pizza with {pizza['crust']} crust "
      f"and the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

print()

favorite_languages = {
    'john': ['python','rust'],
    'amy': ['c'],
    'edward': ['rust','go'],
    'paul': ['python','c#']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite programming languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite programming language is:")
        for language in languages:
            print(f"\t{language.title()}")  
print()       

# Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maria',
        'last': 'skłodowska-curie',
        'location': 'paryż',
    },
}

for username, user_info in users.items():
    print(f"\nUser name: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tName and surname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
print()

person_01 = {
    'first_name' : 'rick',
    'last_name' : 'grimes',
    'age' : 30,
    'city' : 'New York'
}

# for key, value in person.items():
#     print(key, value)

person_02 = {
    'first_name' : 'maggie',
    'last_name' : 'green',
    'age' : 27,
    'city' : 'New York'
}

person_03 = {
    'first_name' : 'beth',
    'last_name' : 'green',
    'age' : 20,
    'city' : 'New York'
}

people = [person_01, person_02, person_03]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name}\nAge: {person['age']}\n"
          f"City: {person['city']}")
    
rabbit = {'name': 'Bunny', 'color': 'white', 'age': 2, 'owner': 'Tom'}
cat = {'name': 'Whiskers', 'color': 'gray', 'age': 3, 'owner': 'Amy'}
dog = {'name': 'Buddy', 'color': 'brown', 'age': 5, 'owner': 'Sasha'}

pets = [rabbit, cat, dog]

for pet in pets:
    print(f"\nName: {pet['name']}\nColor: {pet['color']}\n"
          f"Age: {pet['age']}\nOwner: {pet['owner']}")
    
print()

cities = {
    'Warsaw': {
        'country': 'Poland',
        'population': 1790658  
    },
    'Paris': {
        'country': 'France',
        'population': 2148327 
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286
    }
}

# Display city information
for city, info in cities.items():
    print(f"City: {city}")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
 
