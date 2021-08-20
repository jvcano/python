# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
print(names) 
random_value=len(names)
print(random_value)
random_number = random.randint(0,random_value-1)
print(names[random_number]+ " is going to buy the meal today!")
#using the random.choise from the random library 
person_howpays = random.choice(names)
print(person_howpays + " is going to buy the meal today!")

