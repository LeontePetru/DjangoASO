from django.urls import path
from . import views

urlpatterns=[
    path('', views.login, name='loginHome'),
    path('login/',views.login,name='login'),
    path('room/<str:room>/<str:username>', views.room, name='room'),
    path('checkCredentials',views.checkCredentials,name='checkCredentials'),
    path('checkRoom',views.checkRoom,name='checkRoom'),
    path('getUserRooms/<str:user>/', views.getUserRooms, name='getUserRooms'),
    path('roomList/<str:user>/', views.roomList, name='roomList'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')
]