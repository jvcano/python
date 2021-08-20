import random 
from time import sleep

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scis =[rock, paper, scissors]

choise =input("pick rock, paper or scissors.\n ")
if choise == 'rock':
  user_value = 0
elif choise == 'paper':
  user_value = 1
else:
  user_value = 2 

random_integer = random.randint(1,3)
if random_integer == 1:
  value_computer = 'rock'
  print("the computer used rock")
  print(rock_paper_scis[0])
  sleep(1)
  print(f"you used {choise}")
  print(rock_paper_scis[user_value])
  if choise == value_computer:
    sleep(0.50)
    print("is a draw")
  elif choise == "paper":
    sleep(0.50)
    print("paper bets rock you win ")
  elif choise == 'scissors':
    sleep(0.50)
    print("rock bets scissors! the computer wins ")

elif random_integer == 2:
  value_computer = 'paper'
  print("the computer used paper")
  print(rock_paper_scis[1])
  sleep(1)
  print(f"you used {choise}")
  print(rock_paper_scis[user_value])
  if choise == 'paper':
    sleep(0.50)
    print("is a draw")
  elif choise == 'rock':
    sleep(0.50)
    print("paper bets rock! the computer wins")
  elif choise == 'scissors':
    sleep(0.50)
    print("scissors bets paper! you win ")
elif random_integer == 3:
  random_computer = 'scissors'
  print("the computer used scissors")
  print(rock_paper_scis[2])
  sleep(1)
  print(f"you used {choise}")
  print(rock_paper_scis[user_value])
  if choise =="scissors":
    sleep(0.50)
    print("is a draw")
  elif choise == 'paper':
    sleep(0.50)
    print ("scissors bets paper! computer wins ")
  elif choise =="rock":
    sleep(0.50)
    print("rock bets scissors! you win")
else:
  sleep(0.50)
  print("you didnt choose well")