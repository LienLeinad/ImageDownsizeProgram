from django.db import models


# Create your models here.
class Images(models.Model):
    #can save the image in this database, if code was written to handle file uploads from JS code, then uncomment this and make sure that the fields are met when saving. 
    img = models.ImageField(upload_to = 'images/')
    # sImg = models.ImageField(upload_to = 'images/sreduced/',blank = True, null = True)       # reduced by 3/4
    # xsImg = models.ImageField(upload_to = 'images/xsreduced/',blank = True,null = True)      # reduced by 1/2
    # xxsImg = models.ImageField(upload_to = 'images/xxsreduced/',blank = True,null = True)    # reduced by 1/4