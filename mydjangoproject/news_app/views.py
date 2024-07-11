from django.shortcuts import render

from news_app.models import Articles


# Create your views here.
def about_new_page(request):
    all_workers = Articles.objects.all()
    return render(request, 'about_new.html', {'object_list': all_workers})  # Изменили context на object_list


