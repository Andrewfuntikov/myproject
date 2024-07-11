"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DeleteView

from myapp1.views import index_page
from mydjangoproject import settings
from news_app.models import Articles
from myapp1.views import adding_system

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],
                              template_name="about_new.html")),
    path('<int:pk>/', DeleteView.as_view(model=Articles, template_name='about_new_post.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
