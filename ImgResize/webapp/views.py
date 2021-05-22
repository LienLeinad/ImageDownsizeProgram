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
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
        return render(request, 'webapp/index.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded!')




