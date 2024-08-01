from django.shortcuts import render
import random

# Create your views here.
n=1
def index(request):
    name='Ashok'
    #no=random.randint(1111,9999)
    global n
    n+=1
    return render(request,'index.html',{'nm':name,'no':n})