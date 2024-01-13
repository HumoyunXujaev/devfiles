from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import TelegramFile
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from .utils import searchFiles
from django.conf import settings
from django.views import View
from django.core.files.base import ContentFile
from django.utils.decorators import method_decorator
import json
import requests
from telegram.ext import Updater
from django.core.files.storage import FileSystemStorage
from users.models import Profile
from django.conf import settings
from django.core.mail import send_mail


@login_required(login_url='login')
def home(request):
    profile = request.user.profile
    context = {'profile':profile,
                }
    return render(request, 'files/index.html', context)

@login_required
def search_files(request):
    profile = request.user.profile
    profile.attempts = profile.attempts - 1
    profile.save()
    files, search_query = searchFiles(request)
    if not files:
        subject = 'New request'
        message = f'Hi Admin, new request has been received. You need to add a new file to db with user_link: {search_query}!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['hujaevhumoyun01@gmail.com'],
            fail_silently=False,
        )

    
    context = {'files': files,'profile':profile,
               'search_query': search_query, }
    return render(request, 'files/search.html', context)

# @login_required
# def search_view(request):
#     if request.method == 'POST':
#         query = request.POST.get('search_query')

#         # Ваш код обработки поискового запроса

#         # Уменьшение попыток для текущего пользователя
#         user_search_attempt, created = SearchAttempt.objects.get_or_create(user=request.user)
#         user_search_attempt.decrease_attempts()

#         # Ваш код дальнейшей обработки запроса и рендеринга шаблона
#         # ...

#     return render(request, 'your_template.html')