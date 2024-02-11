
import re
a=input("Enter debit card number: ")
l=0
for i in [0,2,5,7,10,12,15,17]:
    s=int(a[i]) * 2   
    if s>9:
        c=s//10     #integer division operation hy jo sirf integer hi return karega
        d=s%10
        s=c+d

    l=l+s

final=l+int(a[1])+int(a[3])+int(a[6])+int(a[8])+int(a[11])+int(a[13])+int(a[16])

if not final % 10 == int(a[-1]):
    z=re.search(r"^\d[2-6]{3}\s[2-6]{2}\d{2}\s\d{4}\s\d{4}$", a)
    if z:
      print("Valid debit number")
    else:
      print("Invalid debit number.")

else:
    print("Invalid debit number.")