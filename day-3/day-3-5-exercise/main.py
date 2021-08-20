# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1= input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

print(lowercase_name1)
print(lowercase_name2)

letter_t = lowercase_name1.count('t')
letter_T = lowercase_name2.count('t')

value_t = letter_t + letter_T

letter_r = lowercase_name1.count('r')
letter_R = lowercase_name2.count('r')
value_r = letter_r + letter_R

letter_u = lowercase_name1.count('u')
letter_U = lowercase_name2.count('u')
value_u = letter_u + letter_U

letter_e = lowercase_name1.count('e')
letter_E = lowercase_name2.count('e')
value_e = letter_e + letter_E

letter_l = lowercase_name1.count('l')
letter_L = lowercase_name2.count('l')
value_l = letter_l + letter_L

letter_o = lowercase_name1.count('o')
letter_O = lowercase_name2.count('o')
value_o = letter_o + letter_O

letter_v = lowercase_name1.count('v')
letter_V = lowercase_name2.count('v')
value_v = letter_v + letter_V

print(f"T occurs {value_t} times")
print(f"R occurs {value_r} time")
print(f"U occurs {value_u} times")
print(f"E occurs {value_e} times")
total_true = value_t + value_r + value_u + value_e
print(f"total {total_true}")

print(f"L occurs {value_l} time")
print(f"O occurs {value_o} times")
print(f"V occurs {value_v} times")
print(f"E occurs {value_e} times")
total_love = value_l + value_o + value_v + value_e
print(f"total {total_love}")
sums_total = total_true + total_love
tostring_score = str(sums_total)
score= int(tostring_score)

if score < 10 or score > 90:
  print("Your score is: " + tostring_score + " you go together like coke and mentos") 
elif score >=40 and score <=50 : 
  print("Your score is: " + tostring_score + " you are alright together.")
else:
  print("Your score is: " + tostring_score )