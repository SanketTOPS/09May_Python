from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=StudSerial(stdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial=StudSerial(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)