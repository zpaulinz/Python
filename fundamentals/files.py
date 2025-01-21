# Reading An Entire File:
from pathlib import Path

path = Path('fundamentals/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

print()


# Reading Line By Line:
from pathlib import Path

path = Path('fundamentals/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
    
print()


# Reading Line By Line (Better):
from pathlib import Path

path = Path('fundamentals/pi_digits.txt')
contents = path.read_text()
for line in contents.splitlines():
    print(line)
    
print()



# Working With File Content:
from pathlib import Path

path = Path('fundamentals/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(f"{pi_string[:52]}")
print(len(pi_string))

birthday = input("Enter your birthdate (in the format ddmmyy): ")
if birthday in pi_string:
    print("Your birthdate is among the first million digits of Pi!")
else:
    print("Your birthdate is not among the first million digits of Pi.")

print()
message = "My favorite animal is a dog."
message = message.replace('dog', 'cat')
print(message)

pi_string = pi_string.replace('5', 'ok')
print(pi_string[:52])

print()


# Saving Data To A File:
from pathlib import Path

path = Path('fundamentals/programming.txt')
path.write_text("Aurelia likes programming.")


# Saving Multiple Lines:
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating games.\n"
contents += "I love working with data.\n"

path = Path('fundamentals/programming.txt')
path.write_text(contents)


name = str(input("Please enter your name: "))
path = Path('fundamentals/guest.txt')
path.write_text(name)


guest_names = []
content = ''
while len(guest_names) < 4:
    guest_name = str(input("Please enter your name: "))
    print(f"\nHello {guest_name}")  
    guest_names.append(guest_name)
    content += f"{guest_name}\n"  
    

path = Path('fundamentals/guest_book.txt')
path.write_text(content)
    

    
    