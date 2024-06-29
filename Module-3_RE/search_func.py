import re


mystr="This is Python!"

x=re.search('This',mystr)

print(x)

if x:
    print("Match done!")
else:
    print("Error!")
