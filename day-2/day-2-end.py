#PEMDA () then multiplication divicion sum and finally subtraction
print(3*2)
print(6/2)
print(3+5)
print(7-4)

#other calculation
print(9%3)
print(2**2)

#BMI calculador
print("we will mesuare your body composition or BMI")
weigth = float(input("please introduce your weight in kilograms "))
height = float(input("please introduce your height in meters "))
BMI = weigth / height**2 
BMI_int = int(BMI)
print(type(weigth))
print(type(height))
print("your BMI is " + str(BMI))
print("your BMI is " + str(BMI_int))

# manipulating values += -= /= *=
score = 0 
score += 1

# f-string 
print("this is how f-string works")
print(f"your BMI is {BMI}")
print(f"your BMI is {BMI_int}")