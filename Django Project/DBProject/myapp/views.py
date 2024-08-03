from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        new=studForm(request.POST)
        if new.is_valid():
            new.save()
            print("Record inserted!")
        else:
            print(new.errors)
    return render(request,'index.html')