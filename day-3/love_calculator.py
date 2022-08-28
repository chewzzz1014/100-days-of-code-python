print("Welcome to Love Calculator")
name1 = input("What's your name? ")
name2 = input("What's your name? ")

combined_name = (name1 + name2).lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

score = true + love

if score<10 or score> 90:
    print(f"Your love score is {score}, you go together like coke and mentos")
elif score<=50 or score>=40:
    print(f"Your love score is {score}, you are alright together")
else:
    print(f"Your score is {score}")