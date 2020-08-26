from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    displayname = models.CharField(max_length=90, blank=True, null=True)

    REQUIRED_FIELDS = ['displayname']

    def __str__(self):
        return self.username
