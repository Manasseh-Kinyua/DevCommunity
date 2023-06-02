from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Project, Tag
from .utils import searchProjects, paginateProjects
from .forms import ProjectForm, ReviewForm

# Create your views here.

def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {
        'projects': projects,
        'search_query': search_query,
        # 'paginator': paginator,
        'custom_range': custom_range,
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        project.getVoteCount

        messages.success(request, "Review was added successfully")
        return redirect('project', pk=project.id)

    context = {
        'project': project,
        'form': form,
    }
    
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Project was added successfully")
            return redirect('account')

    context = {
        'form': form
    }

    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project was modified successfully")
            return redirect('account')

    context = {
        'form': form
    }

    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    context = {
        'object': project
    }
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project was deleted successfully")
        return redirect('account')

    return render(request, 'delete_template.html', context)