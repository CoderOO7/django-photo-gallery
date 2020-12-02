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

    return render(request,'app/home.html',context)

def details(request, image_id):
    image = get_object_or_404(GalleryImage, pk=image_id)
    return render(request,'app/details.html',{'image':image})

def image_upload(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST,request.FILES)
        if form.is_valid():
            newImage = form.save(commit=False)
            newImage.save()
            #to save input tags below function
            form.save_m2m()
            return redirect('home')
        else:
            print(form.errors)
        
    return render(request,'app/image/upload.html')
