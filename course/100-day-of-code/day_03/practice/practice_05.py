'''BMI Calculator with interpretations'''

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight / height ** 2

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")