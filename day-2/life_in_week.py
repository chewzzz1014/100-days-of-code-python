# accept age, and display number of days, weeks, months the person left if he/she lives until 90 years old

age = int(input("Enter age: "))

years_input = 90 - age
months_input = years_input * 12
weeks_input = years_input * 52
days_input = years_input * 365

print(f"You have {days_input} days, {weeks_input} weeks, and {months_input} months left.")