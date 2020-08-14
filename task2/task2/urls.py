"""task2 URL Configuration

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
from django.urls import path
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_view.signup,name= 'user-signup'),
    path('logged_in/',user_view.success,name = 'success'),
    path('logged_out/',user_view.log_out,name = 'logoutsuccessful'),
    path('login/',user_view.log_in,name = 'login'),
]
