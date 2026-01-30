from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=3)
    course = models.CharField(max_length=50)
    images = models.ImageField(upload_to='userProfile/')
