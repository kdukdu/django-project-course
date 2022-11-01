from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    description = models.TextField(verbose_name='Task')
    on_create = models.DateTimeField(auto_now=True)
    on_modified = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')


class Tag(models.Model):
    name = models.CharField(verbose_name='Tag', max_length=50)

    def __str__(self):
        return self.name
