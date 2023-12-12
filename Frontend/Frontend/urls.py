"""
URL configuration for Frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('register/', views.password_register, name='register'),
    path('create_polls/', views.create_polls, name='create_polls'),
    path('create_survey/', views.create_survey, name='create_survey'),
    path('private_office/', views.private_office, name='private_office'),
    path('my_surveys/', views.my_surveys, name='my_surveys'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('faq/', views.faq, name='faq')
]
