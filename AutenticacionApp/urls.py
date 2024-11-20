from django.urls import path

from .views import user_login, user_register, inicio,user_logout,home,  rest_login,rest_register,profile,validate_token

urlpatterns = [
    path('rest/login/', rest_login, name='login'),
    path('rest/register/', rest_register, name='register'),
       path('rest/profile/', profile, name='perfil'),
          path('validate/', validate_token, name='validacion'),

    path('inicio/', inicio, name='inicio'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),  # URL para cerrar sesión
    path('', home, name='home'),  # URL para cerrar sesión


]