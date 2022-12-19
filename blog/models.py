from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

from main import settings


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey('CustomUser', related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.publish.strftime('%Y'),
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])

    class Meta:
        ordering = ('-publish',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField('Comment')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.body}'

    class Meta:
        ordering = ('created',)


class CustomUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                unique=True,
                                on_delete=models.CASCADE,
                                related_name='custom_user')
    first_name = models.CharField("First name", max_length=150, blank=True)
    last_name = models.CharField("Last name", max_length=150, blank=True)
    email = models.EmailField("Email", blank=False, unique=True)
    profile_picture = models.ImageField(upload_to='blog/users/profile_pictures/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
