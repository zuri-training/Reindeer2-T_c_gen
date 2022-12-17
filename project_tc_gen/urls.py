from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacyPolicy, name='privacy-policy'),
    path('tandc/', views.termsAndConditions, name='tandc'),
    path('contact-us/', views.contactUs, name='contact-us'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('newdash/', views.newdash, name='newdash'),
    path('profile/', views.profile, name='profile'),
    path('TC-templates/', views.TCtemplates, name='tctemplates'),
    path('verification/', views.verification, name='verification'),
    path('projects/', views.projects, name='project'),

    path('sign-up/', views.signUp, name='sign-up'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('logout/', views.logout, name='logout'),

    path('<str:pk>/', views.error_404, name='error404'),
    
]
