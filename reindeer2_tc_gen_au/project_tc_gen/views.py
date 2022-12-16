from django.shortcuts import render
from django.http import HttpResponse
from users import urls


# Create your views here.
def homepage(request):
    return HttpResponse("This is our homepage! It works!")

def index(request):
    return render(request=request, template_name='tcgen/index.html')

def register(request):
    return render(request=request, template_name='tcgen/register.html')
    