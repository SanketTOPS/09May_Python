fl=open('stdata.txt','a')


n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter your ID:")
    name=input("Enter your Name:")

    fl.write(f"\nID:{id}\nName:{name}")