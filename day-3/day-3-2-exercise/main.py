# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print("we will mesuare your body composition or BMI")
BMI = round(weight / height**2) 
BMI_int = int(BMI)

if BMI <= 18.5:
  print("your BMI is " + str(BMI)+ " you are underweight" )
elif BMI <= 25:
  print(f"your BMI is {BMI}, you are a normal weight")
elif BMI <= 30:
  print("your BMI is " + str(BMI)+ " you are slightly overweight")
elif BMI <= 35:
  print("your BMI is " + str(BMI)+ " you are obese")
else:
  print("your BMI is " + str(BMI)+ " you are clinically obese.")


