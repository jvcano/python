#function with outputs  
def format_name(first_name,last_name):
 formated_first_name=first_name.upper()
 formated_last_name = last_name.title()
 return f"{formated_first_name} {formated_last_name}"
def letter_number(name, last_name):
  count_first_name = len(name)
  count_last_name = len(last_name)
  total = count_first_name + count_last_name
  return total
formated_string = format_name("jose", "Cano")
print(formated_string)
total = letter_number("jose", "Cano")
print(total)