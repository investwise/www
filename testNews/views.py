from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsItem
from django.utils import timezone

def news_list(request):
    newsList = NewsItem.objects.filter(news_time__lte=timezone.now()).order_by('time')
    return render(request, 'testNews/news_list.html', {'newsList':newsList})
