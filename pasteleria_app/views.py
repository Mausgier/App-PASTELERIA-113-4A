from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

from django.contrib.auth import (
    authenticate,
    login as iniciar_sesion,
    logout as cerrar_sesion,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


# Página principal de la pastelería.
def inicio(request):
    return render(
        request,
        'pasteleria_app/inicio.html'
    )


# Página HTML de inicio de sesión.
def login_pagina(request):

    # Si el usuario ya inició sesión,
    # redirigirlo al listado de productos.
    if request.user.is_authenticated:
        return redirect('pasteleria_app:listar_productos')

    # Si no está autenticado, mostrar el login.
    return render(
        request,
        'pasteleria_app/login.html'
    )


# Página HTML para listar productos.
@login_required
@require_GET
def listar_productos(request):
    return render(request, 'pasteleria_app/lista.html')


# Página HTML para crear productos.
@login_required
@require_GET
def crear_producto(request):
    formulario = ProductoForm()

    return render(
        request,
        'pasteleria_app/crear.html',
        {'formulario': formulario}
    )


# Página HTML para consultar un producto.
@login_required
@require_GET
def detalle_producto(request, id):
    return render(
        request,
        'pasteleria_app/detalle.html',
        {'id': id}
    )


# Página HTML para editar un producto.
@login_required
@require_GET
def editar_producto(request, id):
    formulario = ProductoForm()

    return render(
        request,
        'pasteleria_app/editar.html',
        {
            'id': id,
            'formulario': formulario
        }
    )


# Página HTML de confirmación de eliminación.
@login_required
@require_GET
def eliminar_producto(request, id):
    return render(
        request,
        'pasteleria_app/eliminar.html',
        {'id': id}
    )


# API REST para autenticar usuarios.
@method_decorator(csrf_protect, name='dispatch')
class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):

        # Comprobar que se reciba un objeto 'JSON'.
        if not isinstance(request.data, dict):
            return Response({
                'error': 'Debes enviar un objeto JSON.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Recibir credenciales.
        username = request.data.get('username')
        password = request.data.get('password')

        # Validar campos obligatorios y tipos.
        if (
            not isinstance(username, str)
            or not isinstance(password, str)
            or not username.strip()
            or not password
        ):
            return Response({
                'error': 'Debes ingresar usuario y contraseña.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Comprobar credenciales mediante 'Django'.
        usuario = authenticate(
            request=request._request,
            username=username.strip(),
            password=password
        )

        if usuario is None:
            return Response({
                'error': 'Usuario o contraseña incorrectos.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # Obtener o crear el token del usuario.
        token, creado = Token.objects.get_or_create(
            user=usuario
        )

        # Iniciar también la sesión tradicional de 'Django'.
        iniciar_sesion(request._request, usuario)

        return Response({
            'mensaje': 'Autenticación correcta.',
            'usuario': usuario.username,
            'token': token.key
        }, status=status.HTTP_200_OK)


# Cierre de sesión.
@login_required
@require_POST
def logout_pagina(request):

    # Invalidar el token del usuario.
    Token.objects.filter(user=request.user).delete()

    # Cerrar la sesión de 'Django'.
    cerrar_sesion(request)

    return redirect('pasteleria_app:login_pagina')


# Endpoint protegido para comprobar autenticación.
class PerfilAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            'mensaje': 'Token válido.',
            'usuario': request.user.username
        }, status=status.HTTP_200_OK)

