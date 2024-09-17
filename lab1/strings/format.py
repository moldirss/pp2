#F-strings
#we can combine strings and numbers by using f-strings or the format() method!
age = 36
txt = f"My name is John,I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars" 
print(txt)

#A placeholder can include a modifier to format the value
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder
txt = f"The price is {59 * 20} dollars"
print(txt)