# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_files, name='search')
    # path('save-telegram-file/', telegram_webhook, name='save_telegram_file'),
    # Добавьте другие маршруты, если необходимо
]
