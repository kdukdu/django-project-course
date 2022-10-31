from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'todolist/index.html')


def about_us(request):
    return render(request, 'todolist/about_us.html')
