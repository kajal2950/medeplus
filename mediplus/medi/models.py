from django.db import models
from enum import unique
from autoslug import AutoSlugField
# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=100,default="")
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name
