from django import forms
from .models import NewsItem

class NewsURL(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ('url',)
