#The format() method formats the specified value(s) and insert them inside the string's placeholder.
text = "For only {price:.2f} dollars."
x = text.format(price = 48)
print(x)