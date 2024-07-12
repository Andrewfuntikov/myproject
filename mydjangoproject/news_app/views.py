from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Articles
from django.shortcuts import render, get_object_or_404


def article_detail(request, id):
    article = get_object_or_404(Articles, id=id)
    context = {
        'article': article,
    }
    return render(request, 'news_details.html', context)


def about_new_page(request):
    all_workers = Articles.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Используйте ArticleForm для формы
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно добавлена!")
            return redirect('news_list')
    else:
        form = ArticleForm()

    context = {
        'object_list': all_workers,
        'form': form
    }
    return render(request, 'about_new.html', context)
