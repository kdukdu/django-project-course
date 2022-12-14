from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    temperature = models.CharField(max_length=10, null=True, blank=True)
    icon = models.CharField(max_length=10, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class CityList(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CityList'
        verbose_name_plural = 'CityLists'
        ordering = ('-pk',)
