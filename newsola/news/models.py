from sre_parse import CATEGORIES
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

class News(models.Model):
    news_text = models.CharField(max_length=150)
    news_picture = models.ImageField(height_field=128,width_field=128)
    news_url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.news_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


