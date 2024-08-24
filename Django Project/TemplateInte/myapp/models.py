from django.db import models

# Create your models here.

class contct(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    sub=models.CharField(max_length=100)
    msg=models.TextField()