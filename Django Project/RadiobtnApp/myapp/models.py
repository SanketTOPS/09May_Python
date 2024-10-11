from django.db import models

# Create your models here.


class usersignup(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
     
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)