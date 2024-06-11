fl=open('test1.txt','w')

id=input("Enter your ID:")
name=input("Enter your Name:")

#fl.write(id)
#fl.write(name)

fl.write(f"ID={id}\nName={name}")