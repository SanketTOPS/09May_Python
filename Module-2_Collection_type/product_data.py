import requests


url="https://fakestoreapi.com/products/"

req=requests.get(url)

data=req.json()

#print(data)

for i in data:
    #print(i)
    print(f"{i['title']} & Price:{i['price']}")
    print(f"Rating:{i['rating']['rate']}")
    print("----------------------------------")
   
    