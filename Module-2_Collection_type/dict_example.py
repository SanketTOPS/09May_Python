stdata={'id':101,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata['sub'])
print(stdata.get('name'))
print(stdata.keys())
print(stdata.values())
print(len(stdata))
"""


"""if 'name' in stdata:
    print("Yes...")
else:
    print("Nooo")
"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    print(i,j)"""

#key=id and Value=1
#key=name and value=sanket


#stdata['id']=102
#stdata['city']='Rajkot' #adding a item
#stdata.pop('sub')
#del stdata['sub']
#stdata.clear()
#del stdata
#print(stdata)


newstdata=stdata.copy()
print(newstdata)