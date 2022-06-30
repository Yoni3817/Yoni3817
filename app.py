# Weight Measurement
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
unit = unit.upper()
if unit == "L":
    weight = int(weight) * 0.453592
if unit == "K":
    weight = int(weight)
# Height Measurement
height = input("Height: ")
unit2 = input("(M)eter or (F)eet: ")
unit2 = unit2.upper()
if unit2 == "F":
    height = float(height) * 0.3048
if unit2 == "M":
    height = float(height)
# BMI calculation
BMI = weight/height**2
if BMI < 18.5:
    print("Your BMI is: "+str(BMI)+",You are underweight.")
elif BMI > 25.0:
    print("Your BMI is: "+str(BMI)+",You are overweight.")
else: print("You are Within the Healthy Weight Range.")
