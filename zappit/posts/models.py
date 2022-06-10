from django.db import models
from django.contrib.auth.models import User


# Create your models here. https://coursehunter.net/course/sozdanie-api-interfeysov-python-kak-profi-freymvork-django-rest?lesson=3


class Post(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
