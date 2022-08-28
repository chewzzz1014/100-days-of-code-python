print("Welcome to Python Pizza")

size = input("Size of pizza? (S/M/L): ")
pepperoni = input("Do you want pepperoni? (Y/N): ")
cheese = input("Do you want extra cheese? (Y/N): ")

price = 0

if size == "S":
    if pepperoni == "Y":
        price = 17
    else:
        price = 15

elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3

elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3

if cheese == "Y":
    price += 1

print(f"Your final bill is: RM{price}")