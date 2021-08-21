# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
  print("hello " + name )
  print("how do you do "+ name )
  print(f"Isn't the weather nice today {name} ")
user=input("what is your name ")
place= input("where are you from ")
greet(user)
#normal calling
def greet_with(name , location):
  print(f"hello {name}")
  print(f"What is it like in {location}")
greet_with(user,place)
#keyword arguments

greet_with(location=place,name=user)