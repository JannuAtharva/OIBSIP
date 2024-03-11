def calculate_bmi(w,h):
    bmi= w/(h**2)
    return bmi

def classify_bmi(bmi):
    if(bmi<18.5):
        return "Underweight"
    elif(18.5 <= bmi < 25):
        return "Normal weight"
    elif(25 <= bmi < 30):
        return "Overweight"
    else:
        return "Obesity"
    

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metre: "))

bmi = calculate_bmi(weight,height)
category = classify_bmi(bmi)

print("Your BMI is :" ,"%.2f" %bmi)
print("You are classified as :",category)



