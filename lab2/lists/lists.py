#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Acces list items
#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Note: The first item has index 0.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#-1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Check if "apple" is present in the list: