a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"
  print("a and b are equal")
else:##The else keyword catches anything which isn't caught by the preceding conditions
    print("a is greater than b")
  

#You can have if statements inside if statements, this is called nested if statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")