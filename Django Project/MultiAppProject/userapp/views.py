from django.shortcuts import render

# Create your views here.

def userindex(request):
    return render(request,'userindex.html')