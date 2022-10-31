from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    task = models.TextField(verbose_name='Task')
    on_create = models.DateTimeField(auto_now=True)
    on_modified = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    tags = models.ForeignKey('Tag', on_delete=models.PROTECT, related_name='tasks')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(verbose_name='Tag', max_length=50)

    def __str__(self):
        return self.name
