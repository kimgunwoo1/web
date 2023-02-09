from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.photo_list,name='photo_list'),
    path('photo/<int:pk>/',views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/edit/',views.photo_edit,name='photo_edit'),

    path('photo/new/',views.photo_post,name='photo_post'),
    path('photo/<int:pk>/delete',views.photo_del,name='delete_proc'),
    path('download/<str:filename>',views.download_proc,name='download'),

    # http://127.0.0.1/~~~   => photo.urls
]