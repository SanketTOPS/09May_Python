from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from .forms import *
from .models import *


# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            fnm=newuser.cleaned_data['firstname']
            lnm=newuser.cleaned_data['lastname']
            unm=newuser.cleaned_data['email']
            pas=make_password(newuser.cleaned_data['password'])
            ct=newuser.cleaned_data['city']
            st=newuser.cleaned_data['state']
            mob=newuser.cleaned_data['mobile']
            user=usersignup(firstname=fnm,lastname=lnm,email=unm,password=pas,city=ct,state=st,mobile=mob)
            user.save()
            print("User created!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def userlogin(request):
    if request.method=='POST':
        unm=request.POST.get('email')
        user = usersignup.objects.get(email=unm)
        pas=request.POST.get('password')
        encoded_password =  user.password
        check=check_password(password=pas,encoded=encoded_password)
        if usersignup.objects.filter(email=unm).exists() and check is True:
            print("Login Successfull!")
        else:
            print("Error")

    return render(request,'login.html')