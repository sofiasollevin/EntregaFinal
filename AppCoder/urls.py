from django.urls import path
from AppCoder import views
from AppChat import views3

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('selecciones', views.selecciones, name="Selecciones"),
    path('noticias', views.noticias, name="Noticias"),
    path('noticias/noticia1', views.noticia1, name="Noticia1"),
    path('contactos', views.contactosFormulario, name="Contactos"),
    path('login', views.usuarioFormulario, name="Usuarios"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('selecciones/jugadoresFormulario', views.jugadoresForm, name="JugadoresFormulario"),
    path('error', views.error, name="Error"),
    path('AppChat', views3.home, name="AppChat"),
    path('<str:room>/', views3.room, name='room'),
    path('checkview', views3.checkview, name='checkview'),
    path('send', views3.send, name='send'),
    path('getMessages/<str:room>/', views3.getMessages, name='getMessages'),

]