from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        newreq=studForm(request.POST)
        if newreq.is_valid(): #TRUE
            newreq.save()
            print("Record inserted!")
        else:
            print(newreq.errors)
    return render(request,'index.html')


def showdata(request):
    data=studinfo.objects.all()
    return render(request,'showdata.html',{'data':data})