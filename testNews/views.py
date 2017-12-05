from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsItem
from django.utils import timezone

def news_list(request):
    newsList = NewsItem.objects.filter(time__lte=timezone.now()).order_by('time')
    return render(request, 'testNews/news_list.html', {'newsList':newsList})

def news(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.url = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'testNews/post_edit.html', {'form': form})

'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'tutBlog/post_detail.html', {'post': post})
'''
