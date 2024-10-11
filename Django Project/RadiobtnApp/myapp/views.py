from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    newuser=signupForm()
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup successfully!")
        else:
            #print(newuser.errors)
            newuser=signupForm()

    return render(request,'index.html',{'newuser':newuser})