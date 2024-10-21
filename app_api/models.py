from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# User = get_user_model()


class UserAccount(AbstractUser):
    id = models.UUIDField(default=uuid4, editable=False,
                          unique=True, primary_key=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    id = models.UUIDField(default=uuid4, editable=False,
                          unique=True, primary_key=True)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:50]}'


class Comment(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    owner = models.ForeignKey(to=UserAccount, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner.username} - {self.post.title} - {self.body[:20]}'
