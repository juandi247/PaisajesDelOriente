from django.shortcuts import render
from .form import LoginForm,SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Intentamos autenticar al usuario con email y contraseña
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Generamos un token si el usuario es autenticado
                token, created = Token.objects.get_or_create(user=user)
                
                # Guardamos el token en la sesión (opcional, se puede usar cookies también)
                request.session['auth_token'] = token.key
                
                # Redirigimos al usuario al inicio
                return redirect('inicio')
            else:
                form.add_error(None, "Credenciales incorrectas")
                messages.error(request, "Correo o contraseña incorrectos.")
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})





def user_register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Crear el token para el nuevo usuario
            token, created = Token.objects.get_or_create(user=user)
            
            # Guardamos el token en la sesión
            request.session['auth_token'] = token.key
            
            # Redirigimos al usuario al inicio
            return redirect('inicio')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})




def inicio(request):
    # Verificamos si el token existe en la sesión
    token_key = request.session.get('auth_token')
    if token_key:
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            return render(request, 'inicio.html', {'user': user})
        except Token.DoesNotExist:
            # Si el token no es válido, lo eliminamos
            del request.session['auth_token']
            return redirect('login')
    else:
        # Si no hay token, redirigimos al login
        return redirect('login')
    




from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    # Eliminamos el token de la sesión
    if 'auth_token' in request.session:
        del request.session['auth_token']
    
    # También cerramos la sesión de Django
    logout(request)
    
    # Redirigimos al login con headers que deshabilitan el almacenamiento en caché
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1
    response['Pragma'] = 'no-cache'  # HTTP 1.0
    response['Expires'] = '0'  # Proxies

    return response



from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

def home(request):
    # Verifica si el token está presente en la sesión
    token_key = request.session.get('auth_token')
    
    if token_key:
        try:
            # Intenta obtener el token y el usuario asociado
            token = Token.objects.get(key=token_key)
            # Si el token es válido, redirige al inicio
            return redirect('inicio')
        except Token.DoesNotExist:
            # Si el token no es válido, lo elimina de la sesión y se queda en index
            del request.session['auth_token']
    
    # Si no hay token o el token es inválido, muestra la página de inicio (index)
    return render(request, 'index.html')
