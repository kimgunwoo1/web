from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'todo'
urlpatterns = [
    path('',views.todo_list, name='todo_list'), #메인 리스트
    path('post/',views.todo_post,name='todo_post'), #신규 할일 등록
    path('post/<int:pk>/',views.todo_detail, name='todo_detail'), #할일 상세
    path('<int:pk>/edit/',views.todo_edit, name='todo_edit'), #할일 수정
    path('done/',views.done_list,name='done_list'), #완료한 목록 리스트
    path('done/<int:pk>/',views.todo_done, name='todo_done'), #할일 완료 DB 표기
    path('<int:pk>/delete/',views.todo_delete,name='todo_delete')
]