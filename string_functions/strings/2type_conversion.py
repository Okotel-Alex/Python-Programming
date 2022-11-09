person1 = input("Please enter the name of the first person: ")
age1 = input(f"Please enter the age of {person1}: ")
person2 = input("Please enter the name of the second person: ")
age2 = input(f"Please enter the age of {person2}: ")

try:
  age1 = int(age1)
  age2 = int(age2)
  double_age1 = 2*age1
  double_age2 = 2*age2
  output1 = f"{person1}, twice your age is {double_age1} years."
  output2 = f"{person2}, twice your age is {double_age2} years."
  print(output1,"\n",output2)
except:
  print("There was a problem, please enter numeric values for age")