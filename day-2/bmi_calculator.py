print("Welcome to BIM Calculator")

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height**2)

print(f"Your Body Mass Index (BMI) is {round(bmi, 2)}")