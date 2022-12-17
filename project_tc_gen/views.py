
# from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# from .models import Document
from users.models import Profile

from .forms import CreateUserForm

from .decorators import unauthenticated_user


def home(request):
    user = request.user
    context = {'user':'user'}
    return render(request, 'project_tc_gen/index.html', context)

def privacyPolicy(request):
    return render(request, 'project_tc_gen/privacy-policy.html')

def termsAndConditions(request):
    return render(request, 'project_tc_gen/t&c.html')

@login_required(login_url='sign-in')
def faq(request):
    return render(request, 'project_tc_gen/faq.html')

@login_required(login_url='sign-in')
def about(request):
    return render(request, 'project_tc_gen/about.html')

def contactUs(request):
    return render(request, 'project_tc_gen/contact-us.html')

def signUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            Profile.objects.create(user=user, username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email)
            messages.success(request, f'Account was created for {username}')
            return redirect('sign-in')
    context = {'form': form} 
    return render(request, 'project_tc_gen/sign-up.html', context)

@unauthenticated_user
def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
#             context = {'first_name': request.user.first_name}
            print(request.user.id)
            return render(request, "project_tc_gen/dashboard.html")
        else:
            messages.info(request, 'invalid credentials')
    #         return redirect('sign-in')

    # else:
    #     return render(request, 'project_tc_gen/sign-in.html')

    return render(request, 'project_tc_gen/sign-in.html')


def logout(request):
    if request.method== 'POST':
        auth_logout(request)
        return redirect('sign-in')
    return render(request, 'project_tc_gen/logout.html')

@login_required(login_url='sign-in')
def dashboard(request):
    context = {'first_name': request.user.first_name}
    print(request.user.first_name)
    return render(request, 'project_tc_gen/dashboard.html', context)

@login_required(login_url='sign-in')
def profile(request):
    return render(request, 'project_tc_gen/profile.html')

def TCtemplates(request):
    return render(request, 'project_tc_gen/TandC TEMPLATE.html')

def verification(request):
    return render(request, 'project_tc_gen/verification-page.html')

def projects(request):
    # form = GenerateDocument()
    # obj = Document.objects
    # context = {'form': form}
    ms=['Terms and Conditions', 'Privacy Policy']
    if request.method=='POST':
        generator = request.POST.getlist('generator')
        if generator==['Terms and Conditions']:
            print("terms and conditions")
            return render(request, 'project_tc_gen/generatedt&c.html')
        if generator==['Privacy Policy']:
            print("privacy policy")
            return render(request, 'project_tc_gen/generatedprivacypolicy.html')
        # form = GenerateDocument(request.POST)
        # if form.is_valid():
        #     form.save()
            # return redirect("/")
            # return render(request, 'project_tc_gen/privacy-policy.html')
        # elif form.is_termsandcondition==True:
        #     return render(request, 'project_tc_gen/t&c.html')
    return render(request, 'project_tc_gen/projects.html')

def error_404(request, pk):
    pk=pk
    context={'pk':pk}
    return render(request, 'project_tc_gen/error-page.html', context)

# Create your views here.
