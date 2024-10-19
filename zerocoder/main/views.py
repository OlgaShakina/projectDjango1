from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Это первый проект</h1>')

def new(request):
    return HttpResponse('<h1>Это вторая страница</h1>')

def data(request):
    return HttpResponse('<p>Здесь данные проекта</p>')

def test(request):
    return HttpResponse('<h1>Тестировать проект</h1>')