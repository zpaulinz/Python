# Using json.dumps() And json.loads():
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('fundamentals/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)


contents = path.read_text()
numbers = json.loads(contents)

print(numbers, '\n')


# Saving And Reading User-Generated Data:
# Saving Data Using The JSON Module Is Useful 
# To Avoid Losing Information After The Program Ends.
from pathlib import Path
import json

username = input("What's your name? ") 
path = Path('fundamentals/username.json') 
contents = json.dumps(username)
path.write_text(contents)
print(f"Your name has been saved and will be used later, {username}!")


from pathlib import Path
import json

path = Path('fundamentals/username.json') 
contents = path.read_text()
username = json.loads(contents) 
print(f"Welcome back, {username}!")

print()

from pathlib import Path
import json

path = Path('fundamentals/username.json')

if path.exists(): 
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else: 
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"Your name has been saved and will be used later, {username}!")

print()


# Refactoring:
from pathlib import Path
import json

def get_stored_username(path):
    """Retrieve the name from the file, if it exists."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None 


def get_new_username():
    """
    Ask the user to provide their name, and then save it to a file.
    """
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user using their name."""
    path = Path('fundamentals/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path) 
        print(f"Your name has been saved and will be used later, {username}!")

greet_user()


from pathlib import Path
import json

path = Path('fundamentals/favorite_number.json')

def get_favorite_number(path):
    """Ask user for their favorite number and save it to a file."""
    favorite_number = input("What's your favourite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    
def get_stored_favorite_number(path):
    """Display the favorite number if it's stored, if not, prompt user for it."""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favourite number, it's : {favorite_number}\n")
    else:
        print("I don't know your favourite number yet.")
        get_favorite_number(path)
    
get_stored_favorite_number(path)

print()

from pathlib import Path
import json

def get_stored_user_data(path):
    """Retrieve user data from the file, if it exists."""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return {}

def get_new_user_data(path):
    """
    Ask the user to provide their data (name, phone number, city),
    and save it to a file.
    """
    user_data = {}
    user_data['username'] = input("What's your name? ")
    user_data['phone_number'] = input("What's your phone number? ")
    user_data['city'] = input("Which city are you from? ")

    # Save to file
    contents = json.dumps(user_data, indent=4)
    path.write_text(contents)
    return user_data

def greet_user():
    """Greet the user using their stored data or prompt for new data."""
    path = Path('fundamentals/user_data.json')
    user_data = get_stored_user_data(path)
    
    if user_data:
        # Verify the username
        print(f"Is this your name: {user_data['username']}? (yes/no)")
        response = input("> ").strip().lower()
        if response == 'yes':
            print(f"Welcome back, {user_data['username']}!")
            print(f"Your phone number is: {user_data['phone_number']}.")
            print(f"You are from: {user_data['city']}.")
        else:
            print("It seems you're not the same user. Let's update your details.")
            user_data = get_new_user_data(path)
            print("Thank you! Your new data has been saved:")
            print(f"Name: {user_data['username']}")
            print(f"Phone number: {user_data['phone_number']}")
            print(f"City: {user_data['city']}")
    else:
        print("We couldn't find your data. Please provide your details below:")
        user_data = get_new_user_data(path)
        print("Thank you! Your data has been saved:")
        print(f"Name: {user_data['username']}")
        print(f"Phone number: {user_data['phone_number']}")
        print(f"City: {user_data['city']}")

greet_user()
