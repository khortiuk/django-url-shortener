from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .forms import ShortenerUrlFrom
from .models import Shortener


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ShortenerUrlFrom()
        context = {
            'form': form,
        }
        return render(request, template_name='shortener/index.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ShortenerUrlFrom(request.POST)
        if form.is_valid():
            obj, _ = Shortener.objects.get_or_create(full_url=form.cleaned_data.get('full_url'))
            context = {
                'obj': obj,
                'url': request.build_absolute_uri()
            }
            template = 'shortener/show_url.html'
        else:
            template = 'shortener/index.html'
            context = {
                'form': form,
                # 'errors': form.errors
            }
        return render(request, template_name=template, context=context)


class RedirectView(View):
    def get(self, request, key=None, *args, **kwargs):
        print(key)
        obj = get_object_or_404(Shortener, key=key)
        return HttpResponseRedirect(redirect_to=obj.full_url)
