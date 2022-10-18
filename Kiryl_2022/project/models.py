from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='media/images/')


    def __str__(self):
        return f'{self.title} - {self.technology}'
