import random

names_string = input("Enter a list of names, each separated by ', ': ").split(", ")

print(f"{names_string[random.randint(0, len(names_string)-1)]} will pay the bill!")

