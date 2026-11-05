from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

from django.contrib.auth import (
    authenticate,
    login as iniciar_sesion,
    logout as cerrar_sesion,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

#
# INICIO
# Vista encargada de mostrar la pagina principal de la aplicacion de pasteleria 'pasteleria_app'.
#
def inicio(request):

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/inicio.html'.
    #
    return render(request, 'pasteleria_app/inicio.html')


#
# LISTAR_PRODUCTOS
# Vista encargada de mostrar la pagina responsable de permitir el poder consultar y mostrar los productos almacenados dentro de la base de datos.
#
@login_required
def listar_productos(request):

    #
    # PRODUCTO.OBJECTS.ALL()
    # Obtiene todos los registros del modelo 'Producto' mediante las funciones de 'Django'.
    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-all-objects
    #
    productos = Producto.objects.all()

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/lista.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'productos'.
    #
    return render(request, 'pasteleria_app/lista.html', {'productos': productos})


#
# CREAR_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir recibir, validar y guardar nuevos productos dentro de la base de datos.
#
@login_required
def crear_producto(request):

    #
    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        #
        # Crear una instancia del formulario utilizando los datos especificados.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
        #
        # 'request.POST' corresponde a los datos entregados por el 'POST'.
        #
        formulario = ProductoForm(request.POST)

        #
        # Comprobar que los datos cumplan con las validaciones definidas dentro de nuestro modelo y formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#validation-on-a-modelform
        #
        if formulario.is_valid():

            #
            # Guardar el nuevo producto dentro de la base de datos.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            #
            formulario.save()

            #
            # Redirigir a la pagina de listado de productos.
            # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
            #
            return redirect('pasteleria_app:listar_productos')

    #
    # Si el usuario solo busca solicitar la pagina, mostrar un formulario vacio.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    else:
        formulario = ProductoForm()

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/crear.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'formulario'.
    #
    return render(request, 'pasteleria_app/crear.html', {'formulario': formulario})


#
# DETALLE_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir el poder consultar y mostrar la informacion de un producto especifico mediante su identificador 'id'.
#
@login_required
def detalle_producto(request, id):

    #
    # GET_OBJECT_OR_404
    # Busca un objeto dentro de la clase entregada, y, si no encuentra el objeto, lanza como excepcion 'Http404' en vez de lanzar la excepcion 'DoesNotExist'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404
    #
    # 'Http404' es una excepcion generada por 'Django' que ocurre cuando no se puede encontrar una pagina esperada. Como resultado de esto, 'Django' se encarga de convertir dicha excepcion en una respuesta 'HTTP' con estado '404'.
    # https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404
    #
    # 'DoesNotExist' es una excepcion generada por el 'Object‑Relational Mapper' de 'Django' que ocurre cuando no se puede encontrar un objeto esperado.
    # https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist
    #
    # 'Producto' corresponde a una clase, a partir de la cual, se busca obtener su objeto.
    # 'id=id' corresponde al argumento entregado, el cual, 'Django' utiliza por medio de su 'Object‑Relational Mapper' como una condicion de busqueda, para luego, traducir dicho argumento a una condicion 'SQL'.
    #
    # Estos argumentos resultan en la busqueda de un producto cuyo identificador coincida con el 'id' entregado, y, si es que el producto no existe, 'Django' lanzara la excepcion 'Http404'.
    #
    producto = get_object_or_404(Producto, id=id)

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/detalle.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'producto'.
    #
    return render(request, 'pasteleria_app/detalle.html', {'producto': producto})


#
# EDITAR_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir consultar, validar y actualizar la informacion de un producto existente.
#
@login_required
def editar_producto(request, id):

    #
    # GET_OBJECT_OR_404
    # Busca un objeto dentro de la clase entregada, y, si no encuentra el objeto, lanza como excepcion 'Http404' en vez de lanzar la excepcion 'DoesNotExist'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404
    #
    # 'Http404' es una excepcion generada por 'Django' que ocurre cuando no se puede encontrar una pagina esperada. Como resultado de esto, 'Django' se encarga de convertir dicha excepcion en una respuesta 'HTTP' con estado '404'.
    # https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404
    #
    # 'DoesNotExist' es una excepcion generada por el 'Object‑Relational Mapper' de 'Django' que ocurre cuando no se puede encontrar un objeto esperado.
    # https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist
    #
    # 'Producto' corresponde a una clase, a partir de la cual, se busca obtener su objeto.
    # 'id=id' corresponde al argumento entregado, el cual, 'Django' utiliza por medio de su 'Object‑Relational Mapper' como una condicion de busqueda, para luego, traducir dicho argumento a una condicion 'SQL'.
    #
    # Estos argumentos resultan en la busqueda de un producto cuyo identificador coincida con el 'id' entregado, y, si es que el producto no existe, 'Django' lanzara la excepcion 'Http404'.
    #
    producto = get_object_or_404(Producto, id=id)

    #
    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        #
        # Crear una instancia del formulario utilizando los datos especificados.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
        #
        # 'request.POST' corresponde a los datos entregados por el 'POST'.
        # 'instance=producto' indica que se editara un producto existente en vez de generar un producto nuevo.
        #
        formulario = ProductoForm(request.POST, instance=producto)

        #
        # Comprobar que los datos cumplan con las validaciones definidas dentro de nuestro modelo y formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#validation-on-a-modelform
        #
        if formulario.is_valid():

            #
            # Actualizar los datos del producto existente dentro de la base de datos.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            #
            formulario.save()

            #
            # Redirigir a la pagina de detalle de producto.
            # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
            #
            return redirect('pasteleria_app:detalle_producto', id=producto.id)

    #
    # Si el usuario solo busca solicitar la pagina, mostrar el formulario con sus datos actuales.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    else:
        formulario = ProductoForm(instance=producto)

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/editar.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, los valores son 'formulario' y 'producto'.
    #
    return render(request,'pasteleria_app/editar.html',{'formulario': formulario,'producto': producto})


#
# ELIMINAR_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir consultar y eliminar un producto existente, previamente con confirmacion del usuario.
#
@login_required
def eliminar_producto(request, id):

    #
    # Busca un objeto dentro de la clase entregada, y, si no encuentra el objeto, lanza como excepcion 'Http404' en vez de lanzar la excepcion 'DoesNotExist'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404
    #
    # 'Http404' es una excepcion generada por 'Django' que ocurre cuando no se puede encontrar una pagina esperada. Como resultado de esto, 'Django' se encarga de convertir dicha excepcion en una respuesta 'HTTP' con estado '404'.
    # https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404
    #
    # 'DoesNotExist' es una excepcion generada por el 'Object‑Relational Mapper' de 'Django' que ocurre cuando no se puede encontrar un objeto esperado.
    # https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist
    #
    # 'Producto' corresponde a una clase, a partir de la cual, se busca obtener su objeto.
    # 'id=id' corresponde al argumento entregado, el cual, 'Django' utiliza por medio de su 'Object‑Relational Mapper' como una condicion de busqueda, para luego, traducir dicho argumento a una condicion 'SQL'.
    #
    # Estos argumentos resultan en la busqueda de un producto cuyo identificador coincida con el 'id' entregado, y, si es que el producto no existe, 'Django' lanzara la excepcion 'Http404'.
    #
    producto = get_object_or_404(Producto, id=id)

    #
    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        #
        # Eliminar el producto de la base de datos.
        # https://docs.djangoproject.com/en/5.0/topics/db/queries/#deleting-objects
        #
        producto.delete()

        #
        # Redirigir a la pagina de listado de productos.
        # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
        #
        return redirect('pasteleria_app:listar_productos')

    #
    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/eliminar.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'producto'.
    #
    return render(request,'pasteleria_app/eliminar.html',{'producto': producto})


# Página HTML de inicio de sesión.
def login_pagina(request):

    if request.user.is_authenticated:
        return redirect('pasteleria_app:listar_productos')

    return render(request, 'pasteleria_app/login.html')


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

