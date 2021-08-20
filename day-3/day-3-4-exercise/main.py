# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

small = 15
medium = 20
large = 25 
#Write your code below this line 👇

if size == "S":
  if add_pepperoni == "Y":
    small+=2 
    if extra_cheese == "Y":
      small+=1
      print(f"your total is {small}")
    else:
      print(f"your total is {small}")     
  elif extra_cheese == "Y":
    small+=1
    print(f"your total is {small}") 
  else :
    print(f"your total is {small}")       
elif size == "M":
  if add_pepperoni == "Y":
    medium+=3 
    if extra_cheese == "Y":
      medium+=1
      print(f"your total is {medium}")
    else:
      print(f"your total is {medium}")     
  elif extra_cheese == "Y":
    medium+=1
    print(f"your total is {medium}") 
  else :
    print(f"your total is {medium}")    
elif size == "L":
  if add_pepperoni == "Y":
    large+=3 
    if extra_cheese == "Y":
      large+=1
      print(f"your total is {large}")
    else:
      print(f"your total is {large}")     
  elif extra_cheese == "Y":
    large+=1
    print(f"your total is {large}") 
  else :
    print(f"your total is {large}")    
else:
  print("You didnt select one of the 3 options")
