#Data Types
#string 
print("hello"[0])
print("hello"[4])

#integer 
print(5+6)

#float 

print(21/9)

#boolean true or false
name = input("what is your name ")
if name == "carlos" :
  print("true")
else:
  print("false")

#convert 
a = str(123)
print(type (a))

num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has "+ new_num_char + " characters"  )

#sum de value of 2 numbers
number = input("type a number of two digits ")
print(type(number))
firts_number = int(number[0])
second_number = int(number[1])
sum_number = firts_number + second_number
print(sum_number)