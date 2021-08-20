# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#how she solved it. importan as a matrix

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal-1] = '\U0001F4B0'

#simpler version

map[vertical -1][horizontal-1] = '\U0001F4B0'
#Write your code below this row 👇

#how i solve it
#digits = [int(x) for x in str(position)]
#print(digits)
#if digits[0] == 1:
#  if digits[1] ==1:
#    row1[0]=  '\U0001F4B0'
#  elif digits[1] == 2:
#    row2[0]= '\U0001F4B0'
#  elif digits[1] == 3:
#    row3[0]='\U0001F4B0'
#elif digits[0] == 2:
#  if digits[1] ==1:
#    row1[1]='\U0001F4B0'
#  elif digits[1] == 2:
#   row2[1]='\U0001F4B0'
#  elif digits[1] == 3:
#    row3[1]='\U0001F4B0'
#elif digits[0] == 3:
#  if digits[1] ==1:
#   row1[2]='\U0001F4B0'
#  elif digits[1] == 2:
#    row2[2]='\U0001F4B0'
#  elif digits[1] == 3:
#    row3[2]='\U0001F4B0'
#else:
#  print("insert a valid number")




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")