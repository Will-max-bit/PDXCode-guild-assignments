from django.db import models

# Create your models here.
class UserModel(models.Model):
    profile_picture = models.ImageField(upload_to='images/')