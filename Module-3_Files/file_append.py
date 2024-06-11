fl=open('test1.txt','a')

id=input("Enter your ID:")
name=input("Enter your Name:")

#fl.write(id)
#fl.write(name)

fl.write(f"\nID={id}\nName={name}\n")