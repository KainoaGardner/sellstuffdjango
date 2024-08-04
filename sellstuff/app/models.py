from django.db import models

# Create your models here.
# def User(models.Model):


class Users(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Items(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    sold = models.BooleanField(default=False)
    price = models.FloatField()
    image = models.ImageField(upload_to="static/imgs")
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
