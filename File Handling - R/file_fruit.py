file=open("fruits.txt",'a')

#name=input("Enter fruit name:")
#qty=input("Enter a Qty.:")
#price=input("Enter a price of fruit:")

#file.write(f"Fruit:{name}\nQty:{qty}\nPrice:{price}")

file.close()

file=open("fruits.txt","r+")

data=file.read()

dc=dict()
if "Apple" in data:
    print("you can change...")

    if "Qty" in data:
        qty=input("Enter a Qty.:")
        price=input("Enter a price of fruit:")
        dc["Qty"]=qty
        dc["Price"]=price
        file.write(str(dc))
   
else:
    print("Error")