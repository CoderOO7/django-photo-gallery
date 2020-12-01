from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import GalleryImage

def home(request):
    images = GalleryImage.objects
    return render(request,'app/home.html',{'images':images})

def details(request, image_id):
    image = get_object_or_404(GalleryImage, pk=image_id)
    return render(request,'app/details.html',{'image':image})
