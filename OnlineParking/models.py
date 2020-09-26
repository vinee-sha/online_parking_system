from django.db import models

# Create your models here.
class signUp(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    dateOfBirth = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class book(models.Model) :
    vehicle = models.CharField(max_length=20)
    VehicleNumber = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
