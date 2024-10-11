from django.shortcuts import render

# Create your views here.


def myadmin(request):
    return render(request,'myadmin.html')


def index(request):
    return render(request,'index.html')
