from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        newreq=studForm(request.POST)
        if newreq.is_valid(): #TRUE
            newreq.save()
            print("Record inserted!")
            return redirect('/')
        else:
            print(newreq.errors)
    return render(request,'index.html')


def showdata(request):
    data=studinfo.objects.all()
    return render(request,'showdata.html',{'data':data})


def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        newreq=updateForm(request.POST,instance=stid)
        if newreq.is_valid(): #TRUE
            newreq.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(newreq.errors)
    return render(request,'updatedata.html',{'stid':stid})