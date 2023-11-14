# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='auth-signing-basic.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
