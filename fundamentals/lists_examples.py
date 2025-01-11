# List Examples:
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits)
print(fruits[0],
      fruits[1],
      fruits[2],
      fruits[3],
      fruits[4])
print(fruits[-1])

fruits[2] = 'lemon'
print(fruits, 
      '\n')


# Adding Elements To A List:
fruits.append('strawberry') #Appending an element to the end of a list
print(fruits)

fruits = []
fruits.append('apple')
fruits.append('banana')
fruits.append('lemon')
print(fruits)

fruits = []
fruits.extend(['apple', 'banana', 'lemon', 'grape'])
print(fruits, 
      '\n')


# Inserting Elements Into A List:
animals = ['cat', 'dog']
animals.insert(0, 'rabbit')
print(animals, 
      '\n')


# Removing An Element From A List (Without Using It Later):
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[2])
del fruits[2]
print(fruits)
print(fruits[2], 
      '\n')


# Removing An Element Using The Pop() Method (If You Need The Element After Removal):
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles) 
print(f"The last motorcycle I bought was {last_owned.title()}.\n")


# Removing An Element From Any Position In The List:
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles[0]
print(f"My first motorcycle was {first_owned.title()}.\n")


# Removing An Element By Value:
fruits = ["apple", "banana", "cherry", "orange", "grape"]
fruits.remove('cherry')
print(fruits)

fruits = ["apple", "banana", "cherry", "orange"]
too_sour = 'cherry'
fruits.remove(too_sour)
print(fruits)
print(f"The {too_sour.title()} is too sour for me.\n")
#The remove() method deletes only the first occurrence of the specified value!


# Permanently Sorting A List Using The Sort() Method:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars,
      '\n')


# Temporarily Sorting A list Using The Sorted() Function:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars,
      '\n')


# Displaying A List In Permanent Reverse Order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars,
      '\n')


# Determining The Size Of A List:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars), 
      '\n')




