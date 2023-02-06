from django.contrib import admin #admin을 위해서 만들어준 라이브러리
from . models import Myboard #우리가 정의한 모델을 import
from . models import MyMember

admin.site.register(Myboard)  #Myboard Table을 볼 수 있다
admin.site.register(MyMember)  
