from django.db import models
from users.models import User
from django.utils import timezone

class Twit(models.Model):
    body = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.author.username + ' ' + self.body
    