from termcolor import colored;

#function with outputs  
def format_name(first_name,last_name):
 formated_first_name=first_name.title()
 formated_last_name = last_name.title()
 return f"{formated_first_name} {formated_last_name}"
def letter_number(name, last_name):
  count_first_name = len(name)
  count_last_name = len(last_name)
  total = count_first_name + count_last_name
  return total

name = input("your first name ")
last_name = input('your last name ')
formated_string = format_name(name,last_name)
print(formated_string,'green','on_red')
total = letter_number(name,last_name)
print(total,'green','on_red')