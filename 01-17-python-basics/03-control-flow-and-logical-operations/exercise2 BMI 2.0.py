height = int(input("Enter you height in cm: "))
weight = int(input("Enter your weight in kg: "))

height /= 100

bmi = weight / height ** 2
bmi = float("{:.2f}".format(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif 25 > bmi >= 18.5:
    print(f"Your BMI is {bmi} and you are normal weight")
elif 30 > bmi >= 25:
    print(f"Your BMI is {bmi} and you are overweight")
elif 35 > bmi >= 30:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")



















