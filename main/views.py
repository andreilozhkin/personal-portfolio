from django.shortcuts import render
from .models import Job, Education

def index(request):
    jobs = Job.objects.all()
    education = Education.objects.all()
    context = {
        'jobs': jobs,
        'education': education,
    }
    
    return render(request, 'main/index.html', context)
