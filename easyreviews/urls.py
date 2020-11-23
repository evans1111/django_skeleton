"""easyreviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import home
from accounts.views import login_view, register_view, logout_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='main-home'),
    path('accounts/dashboard/', dashboard_view, name='dashboard'),
    path('accounts/login/', login_view, name='user-login'),
    path('accounts/register/', register_view, name='user-register'),
    path('accounts/logout/', logout_view, name='user-logout'),

    path('accounts/reset-password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('accounts/reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


# Set up gitignore for Secret Key & Email info
# Create VIEWS for PW Resets *****


# Submit email form  // PasswordResetView.as_view()
# Add login/logout logic for nav
# Email sent success message 
# Link to password reset form in email
# Password successfully changed message