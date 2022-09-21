from django.urls import path
from AppChat import views3

urlpatterns = [
    path('AppChat/', views3.home, name='Chat'),
    path('<str:room>/', views3.room, name='room'),
    path('checkview', views3.checkview, name='checkview'),
    path('send', views3.send, name='send'),
    path('getMessages/<str:room>/', views3.getMessages, name='getMessages'),

]