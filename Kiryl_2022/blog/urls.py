from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog-index'),
    path('<int:post_id>', views.blog_detail, name='blog-detail'),
    path('category/<str:category>', views.blog_category, name='blog-category')
]