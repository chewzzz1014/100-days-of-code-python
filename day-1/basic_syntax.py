# F-strings
username = input("Enter username: ")
birthYear = int(input("Enter birthyear: "))
def display():
    print(f"Welcome, {username}! You're {2022-birthYear} years old.")


# _ in for loop when the number in range/item in list not needed
for _ in range(5):
    display()

# round(number, number_of_decimal_places)
print(round(3.245676543, 3))   #3.246
# abs: return absolute number
print(round(-12))   # 12


import random
import random as r
from random import randint
from random import *
print(randint(1, 100))

