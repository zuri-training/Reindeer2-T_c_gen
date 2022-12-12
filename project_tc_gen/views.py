from django.shortcuts import render

def home(request):
    return render(request, 'project_tc_gen/index.html')

# Create your views here.
