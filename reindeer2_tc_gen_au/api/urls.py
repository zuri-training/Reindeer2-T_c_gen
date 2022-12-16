from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )

urlpatterns = [
    path ('', views.getRoutes),
    path ('companys', views.getCompany),
    path ('documents', views.getDocument),
    path ('reviews', views.getReview),
    path ('services', views.getService),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]