from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

admin.site.register(User)
admin.site.register(models.Post)
admin.site.register(models.Comment)

