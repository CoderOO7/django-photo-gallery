from django.shortcuts import render,redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import GalleryImage
from .forms import GalleryImageForm

def home(request):
    images = GalleryImage.objects
    # Show most common tags 
    common_tags = GalleryImage.tags.most_common()[:4]
    context = {
        'common_tags': common_tags,
        'images':images
    }

    return render(request,'app/home.html',{'images':images})

def details(request, image_id):
    image = get_object_or_404(GalleryImage, pk=image_id)
    return render(request,'app/details.html',{'image':image})


    
