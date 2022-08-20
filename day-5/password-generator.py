import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

letter = int(input(("How many letters would you like in your password?\n")))

sym = int(input("How many symbols would you like?\n"))

num = int(input("How many numbers would you like?\n"))

password = []

for c in range(1, letter+1):
    password.append(random.choice(letters))
for s in range(1, sym+1):
    password.append(random.choice(symbols))
for n in range(1, num+1):
    password.append(random.choice(numbers))

random.shuffle(password)
password = "".join(password)
print(f"Your password is ready: {password}")