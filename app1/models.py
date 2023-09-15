from django.db import models

# Create your models here.
class Userdata(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()

