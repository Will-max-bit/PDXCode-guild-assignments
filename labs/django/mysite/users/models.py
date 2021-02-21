from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    profile_picture = models.ImageField(upload_to='images/')

# class Profile(models.Model):
#     user = models.OneToOneField(User)