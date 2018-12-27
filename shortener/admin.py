from django.contrib import admin
from .models import Shortener


# Register your models here.
@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['key', 'full_url']
    readonly_fields = ['opened']
