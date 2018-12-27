from django.forms import ModelForm
from .models import Shortener


class ShortenerUrlFrom(ModelForm):
    class Meta:
        model = Shortener
        fields = ['full_url']
