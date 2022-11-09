def d_age(name, age): #Parameters
  age = int(age)
  double_age = 2 * age
  output = f"{name}, twice your age is {double_age}."
  return output

#print(d_age("Alex",24)) #Arguements
my_name = "Alex"
print(d_age(my_name,23))
