file=open("stdata.txt","r+")

print(file.read())
#print(file.readline())
#print(file.readlines())
#print(file.readlines()[3])

"""if file.readable():
    print("Mode is readable...")
else:
    print("Error!")"""


"""for i in file:
    print(i)"""

file.write("\nNew data")