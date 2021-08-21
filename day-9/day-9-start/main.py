programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  123: "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary )
print("\n")
print(programming_dictionary["Bug"])
print("\n")
print(programming_dictionary[123])

#Adding new items to dictionary 
programming_dictionary["loop"] = "The action of doing something over and over"
print(programming_dictionary)

print(programming_dictionary["loop"])
#create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#wipe an existing dictionary 
#programming_dictionary = {}

#Edit an item in a dictionary 
#programming_dictionary["Bug"] = "hello world"

#loop through a dictionary 
for key  in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#nesting a list in a dictionary 
travel_log ={
"France": ["paris","Lille","Dijon"],#list inside a dictionary
"Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":12},# a dictionary inside of a dictionary  
}

#nesting  dictionary in a list
travel_log_list=[
  {
    "country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits":12
  },
  {
    "country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":5
  },
]