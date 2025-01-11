# String Examples:
first_message = "This is a string."
second_message = 'This is also a string.'
third_message = "This 'is' a string."
fourth_message = 'This "is" also a string.'
fifth_message = "Let's learn Python step by step."
print(f"\n{first_message} {second_message}")
print(f"{third_message} {fourth_message} {fifth_message}\n")


# Whitespace Characters:
print("Python")
print("\tPython")
print("\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript", '\n')


# Letter Case Manipulation:
name = "john smith aNd his CaT"
print(name.title(), 
      name.upper(), 
      name.lower(), 
      name.swapcase(), 
      name.capitalize(), 
      '\n')


# Full Name Example:
first_name = "john"
last_name = "smith"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!", '\n')


# String Property Checks:
message = "1452345"
print(message.isalpha(), 
      message.isdigit(), 
      message.isalnum(), 
      message.isdecimal(), 
      message.isnumeric(), 
      message.isupper(), 
      message.islower(),
      message.istitle(),
      message.isspace(),
      message.isidentifier(),
      message.isprintable(),
      message.isdecimal(),
      '\n') 


# Prefix and Suffix Removal:
wikipedia_url = 'https://en.wikipedia.org'
print(wikipedia_url.removeprefix('https://'))

file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'), '\n')


# Encoding and Decoding:
text = "Hello"
encoded_text = text.encode("utf-8")
print(encoded_text, 
      encoded_text.decode("utf-8"), '\n')


# Searching within Strings:
text = "Hello, world!"
print(text.startswith("Hello"), 
      text.endswith("world!"),
      text.count("Hello"), 
      text.find("Python"),
      '\n')


# String Manipulation:
favorite_language = 'pythonabcdef ag a hijk'
print(favorite_language.replace("a", "x"))
print(favorite_language.replace(' ', ''))
print('apple,banana,cherry'.split(","))
print('-'.join(['apple', 'banana', 'cherry']),
      '\n')


# String Padding and Alignment:
print("42".zfill(5), 
      "42".ljust(5, '0'), 
      "42".rjust(5, '0'), 
      "Python".center(15, '*'),
      '\n')


# How to Expand Tabs to Spaces:
text_with_tabs = "Python\tJava\tC++"
print(text_with_tabs.expandtabs(4))  


# Multiline Text Example:
multiline_text = "First line\nSecond line\nThird line"
lines = multiline_text.splitlines()
print(lines)  # ['First line', 'Second line', 'Third line']


#Additional Examples
text = "Hello, welcome to Python!"
print(text.index("Python"),
      text.rindex("Python"),
      '\n') 


# Other String Methods:
text = "hello world"
translation_table = str.maketrans("hello", "12345")
print(translation_table) # 'h' -> '1', 'e' -> '2', 'l' -> '4', 'o' -> '5'
translated_text = text.translate(translation_table) # "hello world" -> "12445 w5r4d"
print(translated_text,
      '\n')

text = "Zażółć gęślą jaźń"
table = str.maketrans("ąćęłńóśźż", "acelnoszz")
print(text.translate(table)) # "Zazolc gesla jazn"

text = "Hello123"
table = str.maketrans('', '', '0123456789')
print(text.translate(table))  # "Hello"

text = "name,age,city"
table = str.maketrans(',', ';')
print(text.translate(table)) # "name;age;city"

print("HELLO".casefold(), 
      '\n') 

text = "apple,banana,cherry"
print(text.partition(","),
      text.rpartition(","))

favorite_language = ' python '
print(favorite_language.rstrip(),
      favorite_language.lstrip(),
      favorite_language.strip()) 