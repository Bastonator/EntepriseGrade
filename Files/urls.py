from . import views
from django.urls import path
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenVerifyView
from .views import FileUploadView
from rest_framework.routers import DefaultRouter
#from .views import (CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView,LogoutView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
    #path('jwt/create/', CustomTokenObtainPairView.as_view()),
    #path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    #path('jwt/verify/', CustomTokenVerifyView.as_view()),
    #path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view(), name="rest_login"),
    path('logout/', LogoutView.as_view(), name="rest_logout"),
    path('upload/', FileUploadView.as_view(), name="file_upload"),
]