from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from taggit.models import Tag

from .forms import CommentForm, RegisterUserForm, LoginUserForm
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'

    def get_queryset(self):
        if not self.kwargs:
            return Post.objects.all()
        else:
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'].lower())
            return Post.objects.filter(tags__in=[tag])


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             status='published',
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
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    # List of similar posts
    similar_posts = post.tags.similar_objects()[:4]

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'similar_posts': similar_posts
    }
    return render(request, 'blog/post/post_detail.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/post/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog:index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/post/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('blog:index')


def logout_user(request):
    logout(request)
    return redirect('blog:login')
