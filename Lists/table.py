from tabulate import tabulate
names = ["Okotel", "Alex", "Bena", "Melissa", "Ronald"]
ages = [24, 28, 30, 35, 40]
courses = ["CSC", "SE", "Telecom", "Bist", "Civ"]
new_list = [names, ages, courses]
print(tabulate(new_list))
#print(len(courses))