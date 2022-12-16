from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register, name='register'),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    #path('detail/<int:id>/', detail, name='detail'),
    #path('new/', create, name='create'),
    #path('update/<int:id>/', update, name='update'),
    #path('delete/<int:id>/', delete, name='delete'),
]