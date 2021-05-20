from django.db import models
from PIL import Image, ImageEnhance

# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to = 'images/')