from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from taggit.models import Tag

from .forms import CommentForm, RegisterUserForm, LoginUserForm, PostAddForm, ProfileUserForm
from .models import Post, CustomUser


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'

    def get_queryset(self):
        if self.kwargs.get('tag_slug', ''):
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'].lower())
            return Post.objects.filter(status='published', tags__in=[tag])
        return Post.objects.filter(status='published')


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user.custom_user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    # List of similar posts
    similar_posts = post.tags.similar_objects()[:4]

    context = {
        'post': post,
        'comments': comments,
        'form': comment_form,
        'similar_posts': similar_posts
    }
    return render(request, 'blog/post/post_detail.html', context=context)


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.custom_user != post.author:
        return HttpResponse('Unauthorized', status=401)

    form = PostAddForm(instance=post)
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post.title = cd['title']
            post.body = cd['body']
            post.status = cd['status']
            post.tags.clear()
            post.save()
            for tag in cd['tags']:
                post.tags.add(tag)
            return redirect(post)

    return render(request, 'blog/post/post_edit.html', context={'form': form})


@login_required(login_url='/blog/login')
def post_add(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.custom_user
            post.save()
            form.save_m2m()
            return redirect(post)
    else:
        form = PostAddForm()

    context = {
        'form': form
    }
    return render(request, 'blog/post/post_add.html', context=context)


@login_required()
def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        if request.user.custom_user == post.author:
            post.delete()
            return redirect('blog:index')
        return HttpResponse('You are not allowed to do this action!')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        email = form.cleaned_data.get('email')
        CustomUser.objects.create(user=user,
                                  email=email)
        login(self.request, user)
        return redirect('blog:profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/auth/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url or reverse_lazy('blog:profile')


@login_required()
def logout_user(request):
    logout(request)
    return redirect('blog:login')


@login_required(login_url='/blog/register')
def profile(request, username=None):
    if username and username != request.user.username:
        author = get_object_or_404(CustomUser, user__username=username)
    else:
        author = request.user.custom_user

    author_posts = Post.objects.filter(author=author).order_by('-created')
    form = ProfileUserForm(instance=author)
    if request.method == "POST":
        form = ProfileUserForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()

    context = {
        'user': author,
        'form': form,
        'author_posts': author_posts
    }
    return render(request, 'blog/auth/profile.html', context=context)
