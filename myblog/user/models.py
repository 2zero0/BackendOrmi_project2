from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True, null=True)
    profile_img = models.ImageField(upload_to = "profiles/", null=True, blank=True)