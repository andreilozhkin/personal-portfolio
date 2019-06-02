from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'main/index.html', context)
