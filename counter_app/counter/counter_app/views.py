from django.shortcuts import render,HttpResponse

def Index(request):
    return HttpResponse("Hello world")
