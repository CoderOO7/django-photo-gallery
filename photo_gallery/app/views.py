from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(render(request,'app/home.html'))
