from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
import json

# Create your views here.
@api_view(['GET'])
def index(request):
    doc={
        '/':'overview get request only',
        '/list':'return collection of trainee',
        '/delete':'delete trainee post request',
    }
    return Response(doc)

@api_view(['GET'])
def list(requests):
    trainess = Trainee.objects.all()
    if (trainess is not None):
        data = Traineeser(trainess,many=True)
        print(data)
    return Response(data.data)

@api_view(['POST'])
def insert(request):
    print(request.data['name'])
    t=Traineeser(data=request.data)
    if(t.is_valid()):
        t.save()
        return Response(t.data)
    else:
        return Response(status=status.HTTP_306_RESERVED)

@api_view(['PUT'])
def update(request, pk):
    trainee = Trainee.objects.get(pk=pk)
    data = Traineeser(instance=trainee, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete(request,pk):
    trainee = Trainee.objects.get(pk=pk)
    data = Traineeser(instance=trainee, data=request.data)

    if data.is_valid():
        data.delete()
        return HttpResponse("deleted")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)




def callapiget(request):
    url = "http://127.0.0.1:8000/API/list/"
    header = {
        "Content-Type": "application/json",
    }

    result = requests.get(url=url, headers=header)

    if result.status_code == 200:
        context={}
        context['trainees']=Traineeser(data=result.json())
        render(request,'list.html',context)
    return HttpResponse('Something went wrong')

def callapipost(request):
    url = "http://127.0.0.1:8000/API/insert/"
    header = {
        "Content-Type": "application/json",

    }

    data={
        "id":"6",
        "name":"tttaaasssnnniimm",
        "nid": "123",
        "courses":"1"
    }
    result = requests.post(url=url,data=json.dumps(data), headers=header)
    print(result.json())
    if result.status_code == 200:
        return HttpResponse('Successful')
    return HttpResponse('Something went wrong')