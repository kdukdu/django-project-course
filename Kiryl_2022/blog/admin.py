from django.contrib import admin

from .models import Comment, Post, Category

# Register your models here.
admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'modified_on']
    filter_horizontal = ['categories']
    ordering = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_on', 'post']
    ordering = ['author']
