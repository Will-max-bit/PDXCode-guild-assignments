from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')


    def __str__(self):
        return self.user.username + ' - ' + str(self.profile_picture.name)
