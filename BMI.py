def bmi_lbs_in(): #pounds and inches
    weight = input("Please enter your weight in pounds. ")
    height = input("Please enter your height in inches. ")
    weight = float(weight)
    height = float(height)
    if weight<0 or height<0:
        print("Invalid height or weight. Please try again.")
    else:
        weight = weight / 2.2
        height = height * 0.0254
        bmi = weight / (height**2)
        if bmi < 18.5:
            print("Your BMI is %.2f. You are underweight." %bmi)
        elif bmi > 24.9:
            print("Your BMI is %.2f. You are overweight." %bmi)
        else:
            print("Your BMI is %.2f. You have an average weight." %bmi)

def bmi_kg_in(): #kilos and inches
    weight = input("Please enter your weight in kilograms. ")
    height = input("Please enter your height in inches. ")
    weight = float(weight)
    height = float(height)
    if weight<0 or height<0:
        print("Invalid height or weight. Please try again.")
    else:
        height = height * 0.0254
        bmi = weight / (height**2)
        if bmi < 18.5:
            print("Your BMI is %.2f. You are underweight." %bmi)
        elif bmi > 24.9:
            print("Your BMI is %.2f. You are overweight." %bmi)
        else:
            print("Your BMI is %.2f. You have an average weight." %bmi)

def bmi_lbs_cm(): #pounds and centimeters
    weight = input("Please enter your weight in pounds. ")
    height = input("Please enter your height in centimeters. ")
    weight = float(weight)
    height = float(height)
    if weight<0 or height<0:
        print("Invalid height or weight. Please try again.")
    else:
        weight = weight / 2.2
        height = height / 100
        bmi = weight / (height**2)
        if bmi < 18.5:
            print("Your BMI is %.2f. You are underweight." %bmi)
        elif bmi > 24.9:
            print("Your BMI is %.2f. You are overweight." %bmi)
        else:
            print("Your BMI is %.2f. You have an average weight." %bmi)

def bmi_kg_cm(): #kilos and centimeters
    weight = input("Please enter your weight in kilograms. ")
    height = input("Please enter your height in centimeters. ")
    weight = float(weight)
    height = float(height)
    if weight<0 or height<0:
        print("Invalid height or weight. Please try again.")
    else:
        height = height / 100
        bmi = weight / (height**2)
        if bmi < 18.5:
            print("Your BMI is %.2f. You are underweight." %bmi)
        elif bmi > 24.9:
            print("Your BMI is %.2f. You are overweight." %bmi)
        else:
            print("Your BMI is %.2f. You have an average weight." %bmi)

def helper():
    wtype = input("Please choose pounds or kilograms. ")
    htype = input("Please choose inches or centimeters. ")
    if wtype == "pounds" and htype == "inches":
        return bmi_lbs_in()
    elif wtype == "kilograms" and htype == "inches":
        return bmi_kg_in()
    elif wtype == "pounds" and htype == "centimeters":
        return bmi_lbs_cm()
    elif wtype == "kilograms" and htype == "centimeters":
        return bmi_kg_cm()
    else:
        print ("Invalid input. Please try again.")

if __name__ == '__main__':
    print
    helper()
