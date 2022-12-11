from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, auth
from users.models import Profile

def home(request):
    return render(request, 'project_tc_gen/index.html')

def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user.id)
            return redirect("dashboard")
        else:
            messages.info(request, 'invalid credentials')
    #         return redirect('sign-in')

    # else:
    #     return render(request, 'project_tc_gen/sign-in.html')

    return render(request, 'project_tc_gen/sign-in.html')

def logoutConfirm(request):
    return render(request, 'project_tc_gen/logout.html')

def logout(request):
    if request.method== 'POST':
        auth_logout(request)
        return redirect('sign-in')
    return render(request, 'project_tc_gen/logout.html')

def dashboard(request):
    print(request.user.id)
    return render(request, 'project_tc_gen/dashboard.html')

def faq(request):
    return render(request, 'project_tc_gen/faq.html')

def about(request):
    return render(request, 'project_tc_gen/about.html')

def profile(request):
    return render(request, 'project_tc_gen/profile.html')
# Create your views here.
