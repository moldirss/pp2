#Add an item to a set, using the add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#To add items from another set into the current set, use the update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)