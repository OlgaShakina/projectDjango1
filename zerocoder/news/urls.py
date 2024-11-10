from django.urls import path
from . import views
from .views import news_detail


urlpatterns = [
    path('', views.home, name='news_home'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('create_news/', views.create_news, name='add_news')
]
