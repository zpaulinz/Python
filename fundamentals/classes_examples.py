# Classes Examples:

# Classes In Python Should Be Named Using CamelCase, 
# While Instances And Modules Should Be Written In Lowercase 
# With Optional Underscores. Each Class And Module Should Include 
# A Docstring Describing Its Purpose, And Imports Should Be Organized 
# In The Following Order: 
# Standard Libraries First, Followed By Custom Modules."

class Dog:
    """A simple attempt at modeling a dog."""
    def __init__(self, name, age):
        """Initialize the name and age attributes."""  
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate the dog sitting after receiving a command."""
        print(f"{self.name.title()} is now sitting.")
        
    def roll_over(self):
        """
        Simulate the dog rolling over onto its back after 
        receiving a command.
        """
        print(f"{self.name.title()} just rolled over!")

    
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)

print(f"My dog's name is {my_dog.name.title()}.") 
print(f"My dog is {my_dog.age} years old.") 
 
 
# Accessing Attributes:
print(my_dog.name)
    

# Calling Methods:
my_dog.sit()
my_dog.roll_over()


print(f"Your dog's name is {your_dog.name.title()}.") 
print(f"Your dog is {your_dog.age} years old.") 
your_dog.sit()

print()

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): 
        """Initialize attributes that describe the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self): 
        """Displays information about the car's mileage."""
        print(f"This car has {self.odometer_reading} km on it.")
        
    def update_odometer(self, mileage):
        """
        Assign the given value to the car's odometer.
        The change will be rejected if an attempt 
        is made to roll back the odometer.
        """
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the car's odometer!")

    def increment_odometer(self, kilometers):
        """Increment the car's odometer reading by the given value."""
        self.odometer_reading += kilometers
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying Attribute Value:
# Direct Modification Of Attribute Value:
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Modifying Attribute Value Using A Method:
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019) 
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        # Initialize restaurant attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} "
        "restaurant.")

        print(f"Clients served: {self.number_served}")

    def open_restaurant(self):
        """Display the restaurant's opening hours."""
        print("Opening hours: 8:00 AM - 8:00 PM")

    def set_number_served(self, clients):
        """Set the number of clients served to a specific value."""
        if clients >= 0:
            self.number_served = clients
        else:
            print("Number of clients served cannot be negative.")

    def increment_number_served(self, additional_clients):
        """Increment the number of clients served by a given number."""
        if additional_clients > 0:
            self.number_served += additional_clients
        else:
            print("Number of additional clients must be positive.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, 
                 flavors):
        # Initialize attributes of the parent class (Restaurant)
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
        
    def show_flavors(self):
        """Display the available ice cream flavors."""
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
        
# Create an IceCreamStand object with available flavors
ice_cream_stand = IceCreamStand("Ice Cream Paradise", "Dessert", 0, 
                                ['vanilla', 'chocolate', 
                                 'strawberry', 'mint'])
ice_cream_stand.describe_restaurant()  # Inherited method
ice_cream_stand.open_restaurant()  # Inherited method
ice_cream_stand.show_flavors()  # Display the available flavors

# Creating a restaurant object
restaurant = Restaurant("McDonald's", "Fast-Food")
print(restaurant.restaurant_name)  # Display the restaurant name
print(restaurant.cuisine_type)  # Display the type of cuisine

# Display the initial number of clients served
print(f"Initial number of clients served: {restaurant.number_served}")

# Update the number of clients served using set_number_served
restaurant.set_number_served(55)
print(f"Updated number of clients served: {restaurant.number_served}")

# Increment the number of clients served
restaurant.increment_number_served(20)
print(f"Number of clients served after increment:"
      f"{restaurant.number_served}")

# Display restaurant description and opening hours
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating a second restaurant object
kfc = Restaurant("KFC", "Fast-Food")
kfc.describe_restaurant()
kfc.open_restaurant()

# Test set_number_served and increment_number_served on KFC
kfc.set_number_served(100)  # Set initial number of clients
print(f"KFC: Initial number of clients served: {kfc.number_served}")
kfc.increment_number_served(50)  # Increment the number of clients
print(f"KFC: Number of clients served after increment: "
      f"{kfc.number_served}")

print()

class User:
    def __init__(self, first_name, last_name, phone):
        # Initialize user attributes
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.login_attempts = 0  # Adding a login_attempts attribute

    def describe_user(self):
        """Display the user's information."""
        print(f"{self.first_name} {self.last_name}, phone: {self.phone}")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=None):
        """
        Initialize the privileges attribute as a list of strings.
        """
        self.privileges = privileges if privileges is not None else []

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This admin has no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, phone, privileges=None):
        """
        Initialize attributes of the parent class.
        Create a Privileges instance as an attribute.
        """
        super().__init__(first_name, last_name, phone)
        self.privileges = Privileges(privileges)


# Create an Admin object with privileges
admin_user = Admin('Alice', 'Admin', '555123456', [
    "can add post",
    "can delete post",
    "can ban user"
])

# Display admin information
admin_user.describe_user()
admin_user.greet_user()

# Display admin privileges
admin_user.privileges.show_privileges()

print()

# Inheritance:
# init() Method In A Subclass:
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name for the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject any attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, kilometers):
        """Add the given amount to the car's odometer reading."""
        self.odometer_reading += kilometers


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


# Create an instance of ElectricCar
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

# Print the descriptive name of the car
print(my_leaf.get_descriptive_name())


# Defining Attributes And Methods For A Subclass:
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
        
    def describe_battery(self):
        """Display information about the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


# Overriding Parent Class Methods:
class ElectricCar(Car):
    # --cut--
    def fill_gas_tank():
        """An electric car does not have a fuel tank."""
        print("This car does not require refueling!")


# Instance As An Attribute:
#car.py module:
"""
A set of classes designed to represent both 
traditional and electric cars.
"""
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name for the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject any attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, kilometers):
        """Add the given amount to the car's odometer reading."""
        self.odometer_reading += kilometers

class Battery:
    """A simple attempt to model a car's battery."""

    def __init__(self, battery_size=40):  
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):  
        """Display information about the battery's capacity."""
        print(f"This car has a battery with a capacity of "
              "{self.battery_size} kWh.")

    def get_range(self):
        """
        Displays information about the car's range based 
        on the battery capacity.
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"The range of this car is approximately {range} km on "
              "a full charge.")
            
    def upgrade_battery(self):
        """Upgrade the battery to a larger capacity if necessary."""
        if self.battery_size != 65:
            print("Upgrading the battery to 65 kWh...")
            self.battery_size = 65
        else:
            print(f"The battery is already at maximum capacity "
                  "(65 kWh).")
    

class ElectricCar(Car):
    """Represents characteristics of an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()


print()

# Python Standard Library:
from random import randint
print(randint(1, 6), '\n')

from random import choice
players = ['Amy', 'Peter', 'Liam', 'Sam', 'Lia']
first_up = choice(players)
print(first_up, '\n')


from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        number = randint(1, self.sides)
        return number

die_01 = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):  
    print(die_01.roll_die())

die_02 = Die(sides=10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(die_02.roll_die())

die_03 = Die(sides=20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(die_03.roll_die())

print()


from random import sample

numbers = [1, 2, 4, 6, 5, 8, 9, 0, 7, 34, 'a', 'b', 'v', 'c', 'd']

winning_ticket = sample(numbers, 4)

print(f"The ticket which contains {winning_ticket} wins the prize!")


from random import sample

numbers = [1, 2, 4, 6, 5, 8, 9, 0, 7, 34, 'a', 'b', 'v', 'c', 'd']

my_ticket = [8, 7, 'v', 'c']

number_of_iterations = 0

while True:
    winning_ticket = sample(numbers, 4)
    number_of_iterations += 1
    if my_ticket == winning_ticket:
        break

print(f"It took {number_of_iterations} iterations to match the winning"
      " ticket!")
