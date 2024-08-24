from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    return render(request,'appointment.html')

def calltoaction(request):
    return render(request,'calltoaction.html')

def classes(request):
    return render(request,'classes.html')

def contact(request):
    if request.method=='POST':
        newreq=contactForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Your request has been saved!")
        else:
            print(newreq.errors)
    return render(request,'contact.html')

def facility(request):
    return render(request,'facility.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')