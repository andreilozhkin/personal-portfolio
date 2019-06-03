from django.shortcuts import render
from .models import Job, Education, Project, Profile

# exceptions
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    jobs = Job.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()

    try:
        profile = Profile.objects.get(id=1)
    except Profile.DoesNotExist:
        raise ObjectDoesNotExist("Profile instance doesn't exist, please create one")

    context = {
        'jobs': jobs,
        'education': education,
        'projects': projects,
        'profile': profile,
    }

    return render(request, 'main/index.html', context)
