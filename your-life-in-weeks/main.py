age = input("what is your current age ")
years = 70 - int(age)

#long version 

month_default = 70 * 12
month_user = int(age) * 12

weeks_default = 70 * 52.1429 
weeks_user = float(age) * 52.1429

days_default = 70 * 365.2425 
days_user = float(age) * 365.2425

total_month = month_default - month_user
total_weeks = round(weeks_default - weeks_user,1)
total_days = round(days_default - days_user,1)
print(f"You have {years} years left, or {total_month} months left or  {total_weeks} weeks left, or {total_days} days left ")

#sort version  

sort_month = years * 12 
sort_week  = round(years * 52.1429,1)
sort_days  = round(years * 365.2425,1)
print(f"You have {years} years left, or {sort_month} months left or  {sort_week} weeks left, or {sort_days} days left ")