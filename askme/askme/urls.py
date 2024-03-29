"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from question import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_main_page, name='main'),
    path('login/', views.get_login_page, name='login'),
    path('signup/', views.get_signup_page, name='signup'),
    path('ask/', views.get_ask_page, name='ask'),
    path('hot/', views.get_hot_page, name='hot'),
    path('tag/<slug:title>/', views.get_tag_page, name='tag'),
    path('question/<int:num>/', views.get_question_page, name='question'),
    #path('test/<int:year>/', views.index, name='test'),
]
