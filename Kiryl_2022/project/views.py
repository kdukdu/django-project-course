from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def show_all_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/all_projects.html', context=context)


def show_project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project
    }
    return render(request, 'project/one_project.html', context=context)
