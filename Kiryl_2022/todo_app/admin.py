from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
