import keyword

print(keyword.kwlist)

"""x=keyword.kwlist

for i in range(len(x)):
    print(i)"""


x=input("Enter any word:")

if x in keyword.kwlist:
    print("Sorry...This is keyword!")
else:
    print("Good...You can use your own keyword...")