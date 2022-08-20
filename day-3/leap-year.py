print("Welcome to Leap Year")

# is leap year: divisible by 4 and not by 100
# is leap year: divisible by 4, 100, 400

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")

else:
    print(f"{year} is not leap year")