from .models import NewsPost
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter headline news'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short description'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }