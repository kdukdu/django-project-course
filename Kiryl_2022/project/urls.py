from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


app_name = 'project'

urlpatterns = [
    path('', views.show_all_projects, name='index'),
    path('<int:project_id>', views.show_project_detail, name='project-detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
