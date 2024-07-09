from django.shortcuts import render
from myapp1.models import Worker


def index_page(request):
    worker_to_change = Worker.objects.get(id=5)
    all_workers = Worker.objects.all()
    for i in all_workers:
        print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, ID: {i.id} ')
    return render(request, 'index.html')
