mystr="hello python!"

count={}

for i in mystr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)