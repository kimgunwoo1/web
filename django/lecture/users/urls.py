from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signupProcess/', views.signup_process, name='signupProcess'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loginProcess/', views.loginProcess, name='loginProcess'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
		# js, css, image 정적 파일 관리 (Django가 webserver 역할을 함)