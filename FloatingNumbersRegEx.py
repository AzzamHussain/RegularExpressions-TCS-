import re
a=input("Enter float number: ")
z=re.search(r"^\d*\.\d+", a) # \d Returns a match where the string contains digits (numbers from 0-9)	

if z:
    print("it is float")
else:
    print("It is not float")