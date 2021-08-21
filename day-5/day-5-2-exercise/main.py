# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highes_score = 0 
for compare in student_scores:
  
  if highes_score > compare:
    sums = highes_score
  elif highes_score == compare:
    sums = highes_score 
  else:
    sums = compare
    highes_score = compare
print(f"the biggest number is {sums}")


