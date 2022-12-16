from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path("", views.homepage, name="homepage")
    #path('register', views.register, name='register'),
    #path('detail/<int:id>/', detail, name='detail'),
    #path('new/', create, name='create'),
    #path('update/<int:id>/', update, name='update'),
    #path('delete/<int:id>/', delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)