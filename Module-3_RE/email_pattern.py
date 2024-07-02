import re

email=input("Enter an Email:")

email_ptrn="^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$"  #sanket@gmail.com

x=re.findall(email_ptrn,email)

if x:
    print("Email is valid!")
else:
    print("Error!Invalid Email...Try again")