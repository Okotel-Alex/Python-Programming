#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

#Exponents, like ² and ¾ are also considered to be numeric values.

#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
text = "565543"
x = text.isnumeric()
print(x)