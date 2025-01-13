# Input() Function Example:
# message = input(f"Tell me sth about you and I will display "
#                 f"it on the screen: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"Hello {name}!")

# prompt = f"If you tell us who you are, we will personalize the message "
# prompt += "displayed.\nWhat's your name? "
# name = input(prompt)
# print(f"\nHello, {name.title()}!")

# age = int(input("How old are you? "))
# print(age)

# height = input("How tall are you (in centimeters)? ")
# height = int(height)
# if height >= 90:
#     print("\nYou are tall enough for the ride!")
# else:
#     print("\nYou can go on the ride when you grow a little more.")

# Modulo Operator:
print(4 % 3)
print(7 % 2)
print(8 % 5)
print()

# number = input("Enter a number to find out if it is even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# cars = ['audi', 'bmw', 'subaru', 'toyota']
# car_to_rent = input('What brand of car would you like to rent? ')
# message = f"One moment, I'll check if we have a "

# if car_to_rent in cars: 
#     if car_to_rent == 'bmw':
#         print(f"{message}{car_to_rent.upper()} car available.")
#     else:
#         print(f"{message}{car_to_rent.title()} car available.")
# else:
#     print("Sorry, we don't have that car available.")    

# try:
#     table = int(input("How many people should the table be reserved for? "))
#     if table > 8:
#         print("Please wait for a table.")
#     else:
#         print("Your table is ready.")
# except ValueError:
#     print("Please enter a valid integer.")
# try:
#     number = int(input("Please, enter a number: "))
#     if (number % 10) == 0:
#         print("It's a multiple of ten.")
# except ValueError:
#     print("Please enter a valid integer.")


# While Loop:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
print()

# Allowing The User To Decide When To Exit The Program:
# prompt = "\nTell me something about yourself, and I will display it "
# prompt += "on the screen: \nType 'end' to stop the program. "

# message = ""
# while message != 'end':
#     message = input(prompt)
    
#     if message != 'end':
#         print(message)


# Using A Flag:
# prompt = "\nTell me something about yourself, and I will display it "
# prompt += "on the screen: \nType 'end' to stop the program. "

# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'end':
#         active = False
#     else:
#         print(message)
        

# Using The Break Statement To Exit A Loop:
# prompt = "\nEnter the names of cities you would like to visit:"
# prompt += "\n(When you're done listing cities, type 'end'.) "
# while True:
#     city = input(prompt)
#     if city.lower() == 'end':
#         break
#     else:
#         print(f"I would like to visit {city.title()}!")
# You can use the break statement in any Python loop.


# Using The Continue Statement In A Loop:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
    
print()


# Avoiding An Infinite Loop:
x = 1
while x < 6:
    print(x)
    x += 1 # without it -> it's an infinite loop
    
print()   
    
# active = True

# while active:
#     dodatki = input("Jakie chcesz dodatki do pizzy? ")
#     if dodatki == 'end':
#         active = False
#     else:
#         print(f"Dodano: {dodatki}")
        
print() 

# message = "The ticket price is: "

# while True:
#     try:
#         age = int(input("Enter your age (or type 'exit' to quit): "))
        
#         if age < 3:
#             print(f"{message}free")
#         elif age < 13:
#             print(f"{message}10zl")
#         else:
#             print(f"{message}15zl")
        
#         break

#     except ValueError:
#         print("Please enter a valid integer.")
    

# Using While Loop With Lists And Dictionaries:
# Avoid modifying a list in a for loop; use a while loop instead.


# Moving Elements From One List To Another:
unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Weryfikacja użytkownika: {current_user.title()}")
    confirmed_users.append(current_user) 
    
print("\n\tZweryfikowano wymienionych poniżej użytkowników:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")    
    

# Usuwanie z listy wszystkich egzemplarzy określonej wartości
pets = ['pies', 'kot', 'pies', 'złota rybka', 'kot', 'królik', 'kot']
print(pets)
while 'kot' in pets:
    pets.remove('kot')
print(pets)
print()
# # Umieszczenie w słowniku danych wejściowych wprowadzonych przez użytkownika
# responses = {}
# # Ustawienie flagi wskazującej, czy ankieta jest aktywna.
# polling_active = True
# while polling_active:
#     # Prośba o podanie imienia uczestnika ankiety oraz odpowiedzi na pytanie.
#     name = input("\nJak masz na imię? ") 
#     response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia? ")
#     # Umieszczenie odpowiedzi w słowniku:
#     responses[name] = response 
#     # Ustalenie, czy ktokolwiek jeszcze chce wziąć udział w ankiecie.
#     repeat = input("Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie) ") 
#     if repeat == 'nie':
#         polling_active = False
# # Ankieta została zakończona i wyświetlamy jej wyniki.
# print("\n--- Wyniki ankiety ---")
# for name, response in responses.items(): 
# print(f"{name} chciałby się wspiąć na {response}.")



# sandwich_orders = ["1.Kanapka z szynką", "2.Tost", "3.Kanapka z tuńczykiem"]
# finished_sandwiches = []

# for sandwich in sandwich_orders:
    
#     while sandwich_orders:
#         sandwich = sandwich_orders.pop(0)  # Pobierz pierwszy element z listy
#         print(f"\nPrzygotowano: {sandwich}")
#         finished_sandwiches.append(sandwich)  # Przenieś kanapkę na listę wykonanych

# # Wyświetl listę wszystkich zrobionych kanapek
# print("\nOto skończone zamówienia:")
# for sandwich in finished_sandwiches:
#     print(f" - {sandwich}")


# 7.10. Wymarzone wakacje. Przygotuj program pytający użytkowników o ich
# wymarzone wakacje. Program powinien wyświetlać pytanie w stylu: „Jeżeli
# mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał?”.
# Umieść w programie blok kodu odpowiedzialny za wyświetlenie wyników
# przeprowadzonej ankiety.

# Program pytający o wymarzone wakacje

# Inicjalizacja pustej listy, aby przechować odpowiedzi
odpowiedzi = []

# Liczba uczestników ankiety
liczba_ankietowanych = int(input("Ile osób bierze udział w ankiecie? "))

# Pytanie do użytkowników
for i in range(liczba_ankietowanych):
    odpowiedz = input(f"Ankieta {i + 1}: Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał? ")
    odpowiedzi.append(odpowiedz)

# Wyświetlenie wyników ankiety
print("\nWyniki przeprowadzonej ankiety:")
for i, odpowiedz in enumerate(odpowiedzi, start=1):
    print(f"Ankietowany {i}: {odpowiedz}")
