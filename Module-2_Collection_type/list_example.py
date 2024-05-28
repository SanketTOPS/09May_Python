data=['python','java','android','swift','php','python']
"""print(data)
print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])"""

# ---------------------------------------------------------- #

"""print(data)
print(len(data))
data[2]='kotlin'"""

#print(data)

"""for i in data:
    print(i)"""

#print(data.index('swift'))

"""for i in data:
    print(f"{i} = {data.index(i)}")"""

"""n=0
for i in data:
    print(f"{i} = {n}")
    n+=1"""

"""if 'php' in data:
    print("Yes...")
else:
    print("Nooo")"""


# ---------------------------------------------------- #

#print(data)
#data.append('react')
#data.insert(2,'angular')
#data.remove('android')
#data.pop()
#data.pop(0)
#del data[0]
#data.clear()
#data.sort()
#data.reverse()
#del data
print(data)

#newdata=data.copy()
#print(newdata)


#print(data.count('python'))

newdata=['c','c++','ds']
print(newdata)

#print(data+newdata)
data.extend(newdata)
print(data)