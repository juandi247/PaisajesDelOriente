from django.urls import path

from .views import user_login, user_register, inicio,user_logout,home

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', user_logout, name='logout'),  # URL para cerrar sesión
    path('', home, name='home'),  # URL para cerrar sesión


]