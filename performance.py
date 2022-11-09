from tabulate import tabulate


def grade(mylist):
  total = 0
  for x in mylist:
    total = total + x
  average_of_list = total / len(mylist)
  if 80 <= average_of_list <= 100:
    grade = "A"
  elif 70 <= average_of_list < 80:
    grade = "B"
  elif 60 <= average_of_list < 70:
    grade = "C"
  elif 50 <= average_of_list < 60:
    grade = "D"
  elif 40 <= average_of_list < 50:
    grade = "E"
  else:
    grade = "F"
  grades_attained = [grade, average_of_list]
  return grades_attained


student_name = input("Enter the name of the student: ")
no_of_subjects = int(input("Enter the number of subjects: "))
subject_names = []
subject_marks = []

i = 1
while i <= no_of_subjects:
  subject = input(f"Enter the name of subject{i}: ")
  subject_names.append(subject)
  mark = int(input(f"Enter the mark for {subject}: "))
  subject_marks.append(mark)
  i = i + 1

grade_attained = grade(subject_marks)

result = [subject_names, subject_marks]
print(
  f"{student_name} obtained {grade_attained[0]} with an average mark of {grade_attained[1]} and got the scores below"
)
print(tabulate(result))
