from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {
        'caption': "First page Ballet"
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    try:
        return render(request, 'main/contacts.html')
    except Exception as e:
        return HttpResponse(f"Ошибка при загрузке шаблона: {e}")

