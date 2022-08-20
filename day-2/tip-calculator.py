print("Welcome to the Tip Calculator")

total = float(input("What was the total bill? RM"))
num_ppl = int(input("How many people to split the bill? "))
tips_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

amount_per_ppl = ( total * (1 + tips_percentage/100) ) / num_ppl

print(f"Each person should pay: RM{round(amount_per_ppl,2)}")

