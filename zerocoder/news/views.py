from django.shortcuts import render, get_object_or_404
from .models import NewsPost

# Create your views here.
def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(NewsPost, id=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})
