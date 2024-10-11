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


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serail=StudSerial(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method=='GET':
        serail=StudSerial(stid)
        return Response(data=serail.data)

    if request.method=='PUT':
        serail=StudSerial(data=request.data,instance=stid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE','GET'])
def deletedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=StudSerial(stid)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)