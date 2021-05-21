from django.db import models


# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to = 'images/')
    # sImg = models.ImageField(upload_to = 'images/sreduced/',blank = True, null = True)       # reduced by 3/4
    # xsImg = models.ImageField(upload_to = 'images/xsreduced/',blank = True,null = True)      # reduced by 1/2
    # xxsImg = models.ImageField(upload_to = 'images/xxsreduced/',blank = True,null = True)    # reduced by 1/4