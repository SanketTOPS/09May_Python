#stdata={{"id":1,"name":"Sanket"},{"id":2,"name":"Nirav"},{"id":3,"name":"Ashok"}}

#stdata={"id":[1,2,3],"name":["Sanket","Nirav","Mitesh"]}

"""print(stdata)
print(stdata["id"])
print(stdata["name"])"""


"""for i in stdata.values():
    print(i)"""

"""for i,j in stdata.items():
    print(i[0],j[0])"""


# ---------------------------------------------- #
#stdata={"id":[1,2,3],"name":["Sanket","Nirav","Mitesh"]}

stdata={"st1":{"id":1,"name":"Sanket"},"st2":{"id":2,"name":"Nirav"}}

print(stdata)
print(stdata['st1'])
print(stdata['st1']['name'])