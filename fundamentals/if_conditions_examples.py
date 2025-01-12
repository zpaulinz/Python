# If Conditions Examples:
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    # elif car.lower() == 'audi':
    #     print(car)    
    else:
        print(car.title())    
        
print()

# >, <, ==, !=, <=, >= (operators)
requested_fruit = 'apple'
if requested_fruit != 'banana':
    print("Please choose a banana!", 
          '\n')

required_age = 18
age = 17
if age != required_age:
    print('Age 18 is required.', 
          '\n')
    
    
# Checking Multiple Conditions    
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) or (age_1 >= 21))
print()


# Checking If a Value Is In a List:
requested_toppings = ['mushrooms', 'onion', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print()


# Checking If a Value Is Not In a List:
requested_toppings = ['mushrooms', 'onion', 'pineapple']
print('pepperoni' not in requested_toppings,
      '\n')


banned_users = ['john', 'emma', 'michael']
user = 'maria'

if user not in banned_users:
    print(f"{user.title()}, you can post your answer if you want.",
          '\n')


# Boolean Expression:
game_active = True
can_edit = False
print(game_active,
      can_edit)


# If - Else:
age = 17
if age >= 18:
    print("You can vote!")
    print("Have you registered to vote?")
else:
    print("Sorry, you are too young to vote.")
    print("You can register after you turn 18!")


# If - Elif - Else:
age = 12
if age < 4:
    print("The ticket price is 0 PLN.")
elif age < 18:
    print("The ticket price is 25 PLN.")
else:
    print("The ticket price is 40 PLN.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"The ticket price is {price} PLN.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"The ticket price is {price} PLN.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"The ticket price is {price} PLN.")
# The else block runs if no if or elif conditions are met.
# If there's a specific final condition, use elif and skip else.


# If - if
# When you want to check all relevant conditions.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:  # ❶
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nYour pizza is ready!\n")

alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points!')
else:
    pass

alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')

alien_color = 'blue'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')
    
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points!')
if alien_color == 'yellow':
    print('You earned 10 points!')
if alien_color == 'red':
    print('You earned 15 points!')
    
print()

person_age = 1
person_type = ''
if person_age < 2:
    person_type = 'infant'
elif person_age < 4:
    person_type = 'toddler'
elif person_age < 13:
    person_type = 'child'
elif person_age < 20:
    person_type = 'teenager'
elif person_age < 65:
    person_type = 'adult'
else:
    person_type = 'senior'

print(f'You are a {person_type}\n')


favorite_fruits = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print(f"You really like apples!")
if 'banana' in favorite_fruits:
    print(f"You really like bananas!")
if 'orange' in favorite_fruits:
    print(f"You really like oranges!")
    
print()


# Checking For Special Values:   
requested_toppings = ['mushrooms', 'bacon', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nYour pizza is ready!",
      '\n')

requested_toppings = ['mushrooms', 'bacon', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'bacon':
        print("Sorry, we are out of bacon.")
    else:
        print(f"Adding {requested_topping}.")
print("\nYour pizza is ready!\n")


# Checking If The List Is Not Empty:
requested_toppings = []
print()
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nYour pizza is ready!")
else:
    print("Are you sure you want a pizza without toppings?",
          '\n')


# Using Multiple Lists:
available_toppings = ['mushrooms', 'olives', 'bacon', 'pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'fries', 'extra cheese'] 

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we are out of {requested_topping}.")
print("\nYour pizza is ready!\n")


user_names = ['Amy', 'Olivier', 'Tom', 'David', 'admin']

for user_name in user_names:
    if user_name == 'admin':
        print(f"Welcome, admin! Do you want to review today's report?")
    else:
        print(f"Welcome, {user_name}! Thank you for logging in again.")

print()

user_names = []

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Welcome, admin! Do you want to review today's report?")
        else:
            print(f"Welcome, {user_name}! Thank you for logging in again.")
else:
    print(f"We need to find some users!")
    
print()

current_users = ['cAt', 'dog', 'frog', 'turtle', 'hamster']
new_users = ['turtLe', 'snake', 'giraFfe']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"This name '{new_user}' is already taken!")
        print("You should choose another name.")
    else:
        print(f"This name '{new_user}' is available.")
        
print()

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")