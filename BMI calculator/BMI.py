# BMI Calculator in Python

# Taking input for height in meters
h = float(input("Enter your height in meters: "))

# Taking input for weight in kilograms
w = float(input("Enter your weight in Kg: "))

# Calculate BMI
BMI = w / (h * h)

# Print the calculated BMI
print("BMI Calculated is:", BMI)

# Categorize based on BMI value
if BMI > 0:
    if BMI <= 16:
        print("You are very underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("Congrats! You are Healthy")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are very overweight")
else:
    print("Enter valid details")