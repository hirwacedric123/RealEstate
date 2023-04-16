from django.db import models
from django.utils import timezone

# Create your models here.
class House(models.Model):
  category = models.CharField(max_length=255)
  use = models.CharField(max_length=255)
  size =models.CharField(max_length=255)
  rooms = models.IntegerField(null=True)
  baths = models.IntegerField(null=True)
  price =models.CharField(max_length=20)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=20)
  image = models.ImageField(upload_to='shop/images',default='')
  date = models.DateTimeField(default=timezone.now)


  def __str__(self):
    return f"{self.category} {self.address}"
  
class LandPlot(models.Model):
  category = models.CharField(max_length=255)
  use = models.CharField(max_length=255)
  size =models.CharField(max_length=255)
  price =models.CharField(max_length=20)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=20)
  image = models.ImageField(upload_to='shop/images',default='')
  date = models.DateTimeField(default=timezone.now)

