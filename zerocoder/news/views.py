from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.
def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(NewsPost, id=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})


def create_news(request):
    error = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные заполнены некорректно"
    form = NewsPostForm()
    return render(request, 'news/add_news.html', {'form': form, 'errors': error})
