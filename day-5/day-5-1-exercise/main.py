# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total_height=0
for sum in student_heights:
  total_height += sum
print(total_height)

total_student = 0
for students in student_heights:
  total_student += 1
print(total_student)

average = round(total_height / total_student)
print(f"the average is {average}")


