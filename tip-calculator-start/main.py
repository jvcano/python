import colorama;
from termcolor import colored;
from colorama import Fore, Style;

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
amount = float(input(Fore.BLUE+"how much is the bill? "))
people = float(input(Fore.BLUE+"how many people should be splitting the bill? "))
tip    = float(input(Fore.BLUE+"how much you want to tip ? 12% 15% 20% "))

amount_plus_tip =  (tip / 100) * amount
amount_total = round(amount + amount_plus_tip,2)
split_amount= round(amount_total / people,2) 

print(Fore.LIGHTMAGENTA_EX+f"the total plus tip is  {(amount_total)} and each person should pay {split_amount}")
print(colored("the total plus tip is "+ str(amount_total) + " and each person should play " + str(split_amount),'green','on_red'))