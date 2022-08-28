print("Welcome to BIM Calculator")

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height**2)

if bmi < 18.5:
    state = "underweight"
elif bmi < 25:
    state = "normal weight"
elif bmi >= 25 and bmi < 30:
    state = "overweight"
elif bmi>=20 and bmi< 35:
    state = "obese"
else:
    state = "clinically obese"

print(f"Your Body Mass Index (BMI) is {round(bmi, 2)}\n Health State: {state}")