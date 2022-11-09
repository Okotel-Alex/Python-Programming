def d_age(name, age): #Parameters
  age = int(age)
  double_age = 2 * age
  output = f"{name}, twice your age is {double_age}."
  return output

person1 = input("Please enter the name of the first person: ")
age1 = input(f"Please enter the age of {person1}: ")
person2 = input("Please enter the name of the second person: ")
age2 = input(f"Please enter the age of {person2}: ")

try:
  p1 = d_age(person1,age1) #arguements
  p2 = d_age(person2,age2) #arguements
  print(p1,"\n",p2)
except:
  print("There was a problem, please enter numeric values for age")