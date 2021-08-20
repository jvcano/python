print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("you can get in")
else:
  print("Sorry,you cant get in")

age = int(input("what is your age"))
#nested if/else

if height >= 120:
  print("you can get in")
  if age <12:
    print("play 5$")
  elif age <=18:
    print("play 7$")
  else:
    print("please pay 15$")
else:
  print("Sorry,you cant get in")

