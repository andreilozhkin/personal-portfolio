from django.shortcuts import render
from .models import Job, Education, Project

def index(request):
    jobs = Job.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()

    context = {
        'jobs': jobs,
        'education': education,
        'projects': projects,
    }

    return render(request, 'main/index.html', context)
