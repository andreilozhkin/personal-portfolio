from django.shortcuts import render
from .models import Job, Education, Project, Profile, SiteMetaData

# exceptions
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    jobs = Job.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()

    try:
        profile = Profile.objects.all().last
        meta = SiteMetaData.objects.all().last
    except (Profile.DoesNotExist, SiteMetaData.DoesNotExist) as e:
        raise e


    context = {
        'jobs': jobs,
        'education': education,
        'projects': projects,
        'profile': profile,
        'meta': meta,
    }

    return render(request, 'main/index.html', context)
