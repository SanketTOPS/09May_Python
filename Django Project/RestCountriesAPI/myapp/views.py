from django.shortcuts import render
import requests

# Create your views here.

def loadAPI():
    url="https://restcountries.com/v3.1/all"
    req=requests.get(url)
    data=req.json()
    return data
    """for i in data:
        print("Name:",i["name"]["official"])
        print("Region:",i["region"])
        print("Google Map:",i["maps"]["googleMaps"])
        print("Flag:",i["flags"]["png"])"""
    

def index(request):
    apidata=loadAPI()
    return render(request,'index.html',{'data':apidata})