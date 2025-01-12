# Tuple Examples:
my_tuple = (3,) # A tuple is defined by commas inside parentheses.
print(type(my_tuple)) # <class 'tuple'>
coordinates = (10, 20, 30)

not_a_tuple = (42)  # This is just an integer, not a tuple.
print(type(not_a_tuple))  # <class 'int'>

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()


# Iterating Through All Tuple Values:
for dimension in dimensions:
    print(dimension)
    
    
# Overwriting a Tuple:
# A tuple can't be modified \ 
# but you can assign a new value to the variable holding it.
# dimensions[0] = 250 # Returns Error

dimensions = (200, 50)
dimensions = (400, 100)
print(dimensions,
      '\n')

animals = ("dog", "cat", "elephant", "lion", "tiger")

for animal in animals:
    print(animal)

try:
    animals[0] = "rabbit"  
except TypeError as e:
    print(f"Error: {e}")  

animals = ("giraffe", "zebra", "koala", "kangaroo", "panda")

for animal in animals:
    print(animal)
