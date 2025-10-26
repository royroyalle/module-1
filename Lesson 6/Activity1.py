height = float (input("Please enter your height in cm"))
weight = float (input("Please enter your weight in kg"))
bmi = weight/(height/100)**2

if bmi <= 18.9:
    print("You are underweight")
elif bmi <=29.9:
    print("You are healthy")
elif bmi <=39.9:
    print("You are over weight")
elif bmi <=49.9:
    print("You are severely over weight")
elif bmi <=59.9:
    print("You are obese")
else:
    print("You are severely obese")
