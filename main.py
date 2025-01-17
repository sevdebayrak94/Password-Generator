import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?"))
num_symbols = int(input("How many symbols would you like?"))
num_numbers = int(input("How many numbers would you like?"))

password = []

for letter in range(0, num_letters):
    password.append(random.choice(letters))
for num in range(0, num_numbers):
    password.append(random.choice(numbers))
for char in range(0, num_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
#Turn password list to str
password_str = ""
for char in password:
    password_str += char

print(f"Your password is {password_str}")