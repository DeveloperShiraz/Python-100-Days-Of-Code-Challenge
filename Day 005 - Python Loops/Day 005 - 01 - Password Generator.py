
import random # Imports the random module for generating random choices.

# Defines lists of characters for password generation.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcomes the user to the password generator.
print("Welcome to the Password Generator!")

# Prompts the user for the desired number of each character type.
nr_letters= int(input("How many letters would you like in your password? :")) 
nr_symbols = int(input(f"How many symbols would you like? :"))
nr_numbers = int(input(f"How many numbers would you like? :"))

# Base code: Generates a list of password characters.

password_list = []
for char in range(1, nr_letters + 1): # Loops to add random letters.
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1): # Loops to add random symbols.
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1): # Loops to add random numbers.
    password_list += random.choice(numbers)

# Eazy Level: Creates a password string without randomizing order.
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""
for char in password_list: # Concatenates characters into a string.
    easy_password += char
print(f"Your password is: {easy_password}") # Prints the generated easy password.

# Hard Level: Creates a password with randomized character order.
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8
hard_password = ""
random.shuffle(password_list) # Shuffles the order of characters in the list.
for char in password_list: # Concatenates shuffled characters into a string.
    hard_password += char
print(f"Your Shuffled Password is: {hard_password}") # Prints the shuffled password.