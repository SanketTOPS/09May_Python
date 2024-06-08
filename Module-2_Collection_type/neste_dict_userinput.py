stdata={} #root


n=int(input("Enter number of students:"))

for i in range(n):
    st={}
    st=input("Enter your child dict name:")
    stdata[st]={}

    id=input("Enter id:")
    name=input("Enter name:")
    stdata[st]['id']=id
    stdata[st]['name']=name

print(stdata)


