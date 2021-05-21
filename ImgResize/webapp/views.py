from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.files import File
from io import StringIO,BytesIO 
import io
from PIL import Image
# Create your views here.
def index (request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            og = request.FILES['img']
            imgModel = Images()
            imgModel.sImg = resize_uploaded_image(og)
            imgModel.save()
            print("YAY U UPLOADED SOMETHING wooo")
            return redirect('success')
    else:
        form = ImageForm()
        return render(request, 'webapp/index.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded!')


#non view methods
#This method was taken from these sources, but updated to Python 3.7 and slightly changed to manage different sizes instead of just one and returns the image file isntead of saving it directly to the database
#https://www.davedash.com/2009/02/21/resizing-image-on-upload-in-django/
# https://stackoverflow.com/questions/10891626/resizing-uploaded-files-in-django-using-pil
def resize_uploaded_image(i):
    # imagefile = StringIO(i.read)
    image = Image.open(i)


    (width, height) = (1290, 720)
    # (width, height) = scale_dimensions(width, height, longest_side = 240)

    resizedImage = image.resize((width, height))
    #turns image back into a File
    resizedImageFile = io.BytesIO()

    resizedImage.save(resizedImageFile, 'PNG', optimize = True)
    resizedImageFile.seek(0)
    return 


# def resize_uploaded_image(i):
#     image = Image.open(i)
#     img = image.copy()
#     img.thumbnail((1290, 720), Image.ANTIALIAS)
#     return img

