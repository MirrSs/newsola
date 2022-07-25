from django.db import models
from django.utils import timezone
from enum import Enum
import datetime

from django.contrib.auth.models import AbstractUser

LANGUAGE_CHOICE = (
    ("en", "English"),
    ("ru", "Russian"),
    ("de", "Deutsch"),
    ("es", "Espagnol"),
    ("fr", "Français"),
    ("it", "Italiano"),
)

# Create your models here.

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=True)
    language = models.CharField(max_length = 20,default='en')
    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Search(models.Model):
    search_request = models.CharField(max_length=100)

    def __str__(self):
        return self.search_request