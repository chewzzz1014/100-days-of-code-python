print("Welcome to Roller Coaster!")
height = float(input("Enter height in cm: "))
age = int(input("Enter age: "))

if height > 120:
    print("Can ride")
    if age > 18:
        fee = 12
        print("Fee is RM 12")
    elif age < 12:
        fee = 5
        print("Fee is RM 5")
    elif age<=55 and age>= 45:
        print("You get free ride!")
    else:
        fee = 7
        print("Fee is RM 7")

    photo = int(input("Do you want photo? (1 for yes and 0 for no "))
    if photo == 1:
        print(f"Total bills is RM{fee+3}")
    else:
        print(f"Total bill is RM{fee}")
else:
    print("Can't ride")