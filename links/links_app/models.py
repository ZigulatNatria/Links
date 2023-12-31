from django.contrib.auth.models import AbstractUser
from django.db import models


class Collections(models.Model):
    name = models.CharField(verbose_name='название коллекции', max_length=200)
    description = models.TextField(verbose_name='описание')
    date_created = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='время изменения', auto_now=True)


class Bookmark(models.Model):
    TYPE_CHOICE = [
        ('website', 'website'),
        ('book', 'book'),
        ('article', 'article'),
        ('music', 'music'),
        ('video', 'video'),
    ]

    name = models.CharField(verbose_name='название закладки', max_length=200, null=True)
    descriptions = models.TextField(verbose_name='описание', null=True)
    link = models.URLField(verbose_name='ссылка', max_length=500)
    link_type = models.CharField(verbose_name='тип ссылки', max_length=50, default="website")
    preview = models.URLField(verbose_name='превью', max_length=500, null=True)
    date_created = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='время изменения', auto_now=True)
    links_collections = models.ManyToManyField(Collections, verbose_name='коллекции', blank=True)


class CustomUser(AbstractUser):
    username = models.EmailField('email address', unique=True)

    REQUIRED_FIELDS = ["password"]
