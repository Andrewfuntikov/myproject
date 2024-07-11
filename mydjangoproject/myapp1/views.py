from django.shortcuts import render
from myapp1.models import Worker


def index_page(request):
    all_workers = Worker.objects.all()
    return render(request, 'index.html', context={'data': all_workers})


def adding_system(request):
    return render(request, 'adding_system.html')
