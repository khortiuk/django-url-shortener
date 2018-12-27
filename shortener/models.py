from django.urls import reverse_lazy
from django.db import models
from .utils import generate_key


class Shortener(models.Model):
    key = models.CharField(max_length=5, null=False, blank=False, unique=True)
    full_url = models.URLField(null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)
    opened = models.IntegerField(default=0)

    def open(self):
        self.opened += 1
        self.save(update_fields=['opened'])

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_key(self)
        super(Shortener, self).save(*args, **kwargs)

    def __str__(self):
        return self.key
