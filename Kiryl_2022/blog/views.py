from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
def blog_index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_index.html', context=context)


def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/blog_detail.html', context=context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__title__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/blog_category.html', context=context)
