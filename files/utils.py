from .models import TelegramFile
from django.db.models import Q

def searchFiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    
    files = TelegramFile.objects.distinct().filter(
        Q(user_link__icontains=search_query) 
    )
    return files, search_query