from django import forms
from .models import NewsItem

class NewsInput(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ('URL',)
