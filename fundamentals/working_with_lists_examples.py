# Working With Lists Examples:
pets = ['cat', 'dog', 'hamster', 'rabbit']
for pet in pets:
    print(f"{pet.title()} is a pet!")
    
print()


# Creating Numerical Lists:
for value in range(1, 5): #Using the range() function
    print(value)
    
print()

for value in range(5):
    print(value)
    
print()


# Using The Range() Function To Create A List Of Numbers:
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    
print(squares,
      '\n')


# Basic Statistical Data For A List Of Numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits), 
      max(digits), 
      sum(digits))


# List Comprehension:
squares = [value**2 for value in range(1, 11)]
print(squares)

odd_numbers = [odd_number for odd_number in range (1, 21, 2)]
print(odd_numbers)

cubes = [number**3 for number in range(1, 10)]
print(cubes)

cubes = []
for number in range(1,10):
    cubes.append(number**3)
    
print(cubes,
      '\n')


# Working With List Slices:
vegetables = ["carrot", "broccoli", "potato", "cucumber", "lettuce", "onion", "pepper"]
print(len(vegetables))
print(vegetables[0:3])
print(vegetables[:3])
print(vegetables[2:])
print(vegetables[1:3])
print(vegetables[-3:])
print(vegetables[2::2])
print(vegetables[2:7:2],
      '\n')

animals = ['lion', 'tiger', 'leopard', 'cheetah', 'panther', 'elephant', 'zebra']
middle_index = len(animals) // 2
print(middle_index) #3
print("The three elements in the middle of the list are:", animals[middle_index-1:middle_index+2], '\n')


# Iterating Through a Slice
pets = ['cat', 'dog', 'hamster', 'rabbit']
print("Here are our first two animals:")
for pet in pets[:2]:
    print(pet.title())

print()


# Copying a List:
my_pets = ['cat', 'dog', 'hamster', 'rabbit']
friend_pets = my_pets[:]

my_pets.append("turtle")

print(f"My pets: {my_pets}, Friends's pets: {friend_pets} \n")


# Iterating:
animals_in_groups = [['lion', 'tiger'], ['elephant', 'zebra'], ['cheetah', 'panther']]

for group in animals_in_groups:  
    for animal in group: 
        print(animal)
