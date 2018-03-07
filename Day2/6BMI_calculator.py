def calculate(w, h):
    bmi = w * 10000 / (h * h)
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 < bmi < 25:
        print("You have a normal weight.")
    else:
        print("You are overweight.")


print("Let's calculate your BMI (kg/m^2)")
weight = input("Your weight in KG: ")
height = input("Your weight in CM: ")

calculate(float(weight), int(height))
