from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings

# Create your views here.

def index(request):
    return render(request,'index.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def otpverify(request):
    msg=""
    global otp
    print("Your OTP:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("Verification Successfull!")
            msg="Verification Successfull!"
            return redirect('login')
        else:
            msg="Verification Faild...Please try again!"
    return render(request,'otpverify.html',{'msg':msg})

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        username=""
        if newuser.is_valid():
            username=newuser.cleaned_data.get('username')
            try:
                usersignup.objects.get(username=username)
                print("Username is already exists!")
                msg="Username is already exists!"
            except usersignup.DoesNotExist:
                    newuser.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"

                    #Send Email
                    global otp
                    otp=random.randint(11111,99999)
                    sub="Your One Time Password!"
                    msg=f"Dear User\n\nThank you for using our services, Your account has been created with us!\n\nFor Verification purpose, Your One time password is\n{otp}.\n\nThanks & Regrads\nTOPS Technologies - Rajkot\n+91 9724799469 | sanket.tops@gmail.com"
                    from_ID=settings.EMAIL_HOST_USER
                    to_ID=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                    return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'signup.html',{'msg':msg})