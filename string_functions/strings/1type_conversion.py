name = input("Please enter your name: ")
age = input(f"Welcome {name}, please enter your age: ")

try:
 age = int(age)
 double_age = 2*age
 output = f"{name}, twice your age is: {double_age} years"
 print(output)
except:
  print("There was a problem, please enter numeric values for age.")

  