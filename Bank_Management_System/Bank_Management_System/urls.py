"""
URL configuration for Bank_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Bank_Management_System.views import home, create_customer, create_account, deposit, withdraw, delete_customer, get_customer,get_account, update_customer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('create_customer/', create_customer, name="create_customer"),
    path('create_account/', create_account, name="create_account"),
    path('deposit/', deposit, name="deposit"),
    path('withdraw/', withdraw, name="withdraw"),
    path('delete_customer/', delete_customer, name="delete_customer"),
    path('get_customer/', get_customer, name="get_customer"),
    path('get_account/', get_account, name="get_account" ),
    path('update_customer/', update_customer, name="update_customer")
]
