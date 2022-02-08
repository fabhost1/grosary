"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps.views import home,register,register1,login,login1,logout,cart,shop,slide

urlpatterns = [
    path('',home),
    path('logout',logout),
    path('register',register),
    path('register1',register1),
    path('login',login),
    path('login1',login1),
    path('cart',cart),
    path('shop',shop),
    path('slid',slide),
    path('admin/', admin.site.urls),
]
