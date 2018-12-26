from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='base.html')


def sing_in(request):
    return render(request, template_name='sing_in.html')
