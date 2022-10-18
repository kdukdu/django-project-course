from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def blog_index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_index.html', context=context)


def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context=context)
