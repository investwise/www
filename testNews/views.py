from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import NewsItem
from .forms import NewsURL

def news_list(request):
    newsList = NewsItem.objects.filter(time__lte=timezone.now()).order_by('time')
    return render(request, 'testNews/news_list.html', {'newsList':newsList})

def news(request):
    if request.method == "POST":
        form = NewsURL(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.url = request.user
            news.time = timezone.now()
            # html2text logic
            news.title = 'test title'
            news.text = 'test 1 2 3'
            news.save()
            return redirect('news_text', pk=news.pk)
    else:
        form = NewsURL()
    return render(request, 'testNews/news.html', {'form': form})

def news_text(request, pk):
    news = get_object_or_404(NewsItem, pk=pk)
    return render(request, 'testNews/news_text.html', {'news': news})



'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'tutBlog/post_detail.html', {'post': post})
'''
