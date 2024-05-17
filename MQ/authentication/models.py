from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Mission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} | {self.author.username}'

    def get_absolute_url(self):
        return reverse('mission-details', args=[str(self.pk)])

# class Users(models.Model):
#     profile_pic = models.ImageField(null = True, blank=True, upload_to="static/profiles")

