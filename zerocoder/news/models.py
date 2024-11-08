from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect, render


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def create_news(request):
        if request.method == 'POST':
            form = NewsPostForm(request.POST)
            if form.is_valid():
                news_post = form.save(commit=False)
                news_post.author = request.user
                news_post.save()
                return redirect('home')
        else:
            form = NewsPostForm()
        return render(request, 'create_news.html', {'form': form})
