from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login,name='login'),
    #path('<str:room>/', views.room, name='room'),
    path('checkCredentials',views.checkCredentials,name='checkCredentials'),
    path('getUserRooms/<str:user>/', views.getUserRooms, name='getUserRooms'),
    path('roomList/<str:user>/', views.roomList, name='roomList')
]