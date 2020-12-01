from django.shortcuts import render
from django.http import HttpResponse
from .models import GalleryImage

def home(request):
    images = GalleryImage.objects
    return render(request,'app/home.html',{'images':images})
