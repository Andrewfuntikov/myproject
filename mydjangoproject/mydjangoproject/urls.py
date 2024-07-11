from django.contrib import admin
from django.urls import path, include

from myapp1.views import index_page, adding_system
from news_app import views  # Импортируйте ваши представления

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('adding_system/', adding_system),
    path('about_new/', views.about_new_page, name='news_list'),  # Добавьте этот маршрут
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Добавьте этот маршрут
    path('news_app/', include('news_app.urls')),  # Если у вас есть urls.py в news_app
]
