from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session['user']=unm #session created
            return redirect('home')
        else:
            print("Error!Login faild...")
            msg="Error!Login faild..."
    return render(request,'index.html',{'msg':msg})

def signup(request):
    if request.method=='POST':
        newReq=signupForm(request.POST)
        if newReq.is_valid():
            newReq.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newReq.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

