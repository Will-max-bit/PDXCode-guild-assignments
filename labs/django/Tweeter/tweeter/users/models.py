from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=500)


    def __str__(self):
        return self.username + self.phone_number
    


