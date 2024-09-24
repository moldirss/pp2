#Remove "banana" by using the remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)