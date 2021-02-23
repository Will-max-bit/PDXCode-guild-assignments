from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # likes = models.ManyToManyField(User, related_name='blogpost_like')
    blog_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    # def number_of_likes(self):
    #     return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_image(self):
        if self.blog_picture:
            return self.blog_picture.url
        return ''