from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('logout-confirm', views.logoutConfirm, name='logout-confirm'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
]
