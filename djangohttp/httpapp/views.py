from django.shortcuts import render
from django.shortcuts import HttpResponse

def firstmsg(request):
    msg="hello"
    return HttpResponse(msg)

def secondmsg(request):
    msg="hello Sakshi"
    return HttpResponse(msg)

def thirdmsg(request):
    msg="django project"
    return HttpResponse(msg)

def fourthmsg(request):
    msg="http request"
    return HttpResponse(msg)