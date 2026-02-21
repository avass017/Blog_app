from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_Users = models.BooleanField(default=False)

# class Users(models.Model):
#     users_details=
class Users(models.Model):
    users_detail = models.OneToOneField("Login", on_delete=models.CASCADE)
    name = models.CharField()
    email = models.EmailField()
    bio = models.TextField()
    document = models.FileField(upload_to='documents/')

class Blog(models.Model):
    blog_detail = models.ForeignKey("Users", on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField()
    document = models.FileField(upload_to='documents/')
    date = models.DateField()

