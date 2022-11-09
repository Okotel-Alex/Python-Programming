from tabulate import tabulate
name = "John"
phy_names = ["John", "Mike", "Alex", "Jane", "Monica"]
phy_ages = [20, 94, 10, 34, 65]
eng_names = ["Musoke", "Alinaitwe", "Ampaire", "Opio", "Judith"]
new_list = [phy_names, phy_ages, eng_names]
print(tabulate(new_list))
#rint(len(phy_names))