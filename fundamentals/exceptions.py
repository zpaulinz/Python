# Exceptions:

# Handling ZeroDivisionError Exception:
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by 0!")
   
    
# Using Exceptions To Prevent Program Crashes:
print("Enter two numbers to be divided.")
print("Type 'q' to exit the program.")

while True:
    first_number = input("\nFirst number: ") 
    if first_number == 'q':
        break
    second_number = input("Second number: ") 
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number) 
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
        
# Handling FileNotFoundError Exception:
from pathlib import Path

path = Path('fundamentals/alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"We're sorry, but the file {path} does not exist.")
    

# Text Analysis:
else:
    # Calculate the approximate number of words in the file.
    words = contents.split() 
    num_words = len(words) 
    print(f"The file {path} contains {num_words} words.")

print()

# Working With Multiple Files:
from pathlib import Path

def count_words(path):
    """Calculating the approximate word count in a given file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"We're sorry, but the file {path} does not exist.")
    else:
        # Calculate the approximate number of words in the file.
        words = contents.split() 
        num_words = len(words) 
        print(f"The file {path} contains {num_words} words.")

filenames = ['fundamentals/alice.txt', 'siddhartha.txt', 
             'fundamentals/little_women.txt']     
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
print()


# Silent Failure:
def count_words(path):
    """Calculating the approximate word count in a given file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Calculate the approximate number of words in the file.
        words = contents.split() 
        num_words = len(words) 
        print(f"The file {path} contains {num_words} words.")

filenames = ['fundamentals/alice.txt', 'siddhartha.txt', 
             'fundamentals/little_women.txt']     
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
print('ok')


while True:
    try:
        first_input = input('Please enter a first number (or "q" to quit): ')
        if first_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        first_number = float(first_input)
        
        second_input = input('Please enter a second number (or "q" to quit): ')
        if second_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        second_number = float(second_input)
        
        result = first_number + second_number
    except ValueError:
        print("Invalid input. Please enter numeric values only!")
    else:
        print(f"Result: {result}")
        break

print()


# Create the files with pet names
with open("fundamentals/cats.txt", "w") as f:
    f.write("Whiskers\nMittens\nShadow\n")

with open("fundamentals/dogs.txt", "w") as f:
    f.write("Buddy\nMax\nBella\n")

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Content of the file {file_name}:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")

# Try to read the contents of both files
read_file("fundamentals/cats.txt")
read_file("fundamentals/dogs.txt")


# Create the files with pet names
with open("fundamentals/cats.txt", "w") as f:
    f.write("Whiskers\nMittens\nShadow\n")

with open("fundamentals/dogs.txt", "w") as f:
    f.write("Buddy\nMax\nBella\n")

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Content of the file {file_name}:")
            print(content)
    except FileNotFoundError:
        pass

# Try to read the contents of both files
read_file("fundamentals/cats.txt")
read_file("fundamentals/dogs.txt")


from pathlib import Path

path = Path('fundamentals/alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"We're sorry, but the file {path} does not exist.")
else:
    words = contents.split()  
    num_alice = 0  
    for word in words:
        num_alice += word.lower().count('alice')
    print(f"Word 'alice': {num_alice}")
    
    
print()


def count_word(path):
    """Calculating the approximate word count in a given file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()  
        num_word = 0  
        for word in words:
            num_word += word.lower().count('.')
        print(f"Word '.' in {path}: {num_word}")

filenames = ['fundamentals/alice.txt', 'siddhartha.txt', 
             'fundamentals/little_women.txt']     
for filename in filenames:
    path = Path(filename)
    count_word(path)
    