"""mymember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views  # views와 이름이 겹치지 않도록

urlpatterns = [
    #회원가입
    path('admin/', admin.site.urls),
    path('',views.index,name='index'), 
    path('register/',views.register,name='register'),

    #로그인 
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    # 장고가 회원가입 만들어 놓았듯이, 로그인 로그아웃도 만들어 놓은 것임
    # get : login.html 보여주고,  post : 객체 세션에 저장해서 보내줌
    # settings.py  LOGIN_REDIRECT_URL='/result' : 성공하면 /result 로 요청
    path('result/',views.result, name='result'),


    #로그아웃
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
    # settings.py  LOGOUT_REDIRECT_URL='/' : 성공하면 '/' 로 요청

    

]
