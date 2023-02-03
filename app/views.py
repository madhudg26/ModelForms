from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic_modelform(request):
    TMFO=ModelTopicForm()
    d={'form':TMFO}
    if request.method=="POST":
        FD=ModelTopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Topic inserted succesfully')

    return render(request,'topic_modelform.html',d)



def webpage_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}
    if request.method=="POST":
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webpage inserted successfully')


    return render(request,'webpage_modelform.html',d)




def access_modelform(request):
    AMFO=AccessModeForm()
    d={'form':AMFO}
    if request.method=="POST":
        FD=AccessModeForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Access inserted Successfully')

    return render(request,'access_modelform.html',d)