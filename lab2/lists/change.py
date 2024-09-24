#To change the value of a specific item, refer to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #Change the second item

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #Change the second and third value by replacing it with one value:
