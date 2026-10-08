from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


# INICIO
# Vista encargada de mostrar la pagina principal de la aplicacion de pasteleria 'pasteleria_app'.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments
#
def inicio(request):

    # RENDER
    # Permite generar una respuesta 'HTML' utilizando como minimo, el 'request' y 'template_name' entregados.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    return render(request, 'pasteleria_app/inicio.html')


# LISTAR_PRODUCTOS
# Vista encargada de consultar y mostrar los productos almacenados dentro de la base de datos.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments
#
def listar_productos(request):

    # PRODUCTOS = PRODUCTO.OBJECTS.ALL()
    # Obtiene todos los registros del modelo 'Producto' mediante las funciones de 'Django'.
    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-all-objects
    #
    productos = Producto.objects.all()

    # RENDER
    # Permite generar una respuesta 'HTML' utilizando como minimo, el 'request' y 'template_name' entregados.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # El argumento opcional 'context' actuara como un diccionario, el cual, nos permitira acceder a todos los registros desde el 'HTML' utilizando el nombre 'productos'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#optional-arguments
    #
    return render(request, 'pasteleria_app/lista.html', {'productos': productos})


# CREAR_PRODUCTO
# Vista encargada de recibir, validar y guardar nuevos productos dentro de la base de datos.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments
#
def crear_producto(request):

    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        # Crear una instancia del formulario utilizando los datos enviados mediante 'request.POST'.
        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST
        #
        formulario = ProductoForm(request.POST)

        # Comprobar que los datos cumplan con las validaciones definidas dentro de nuestro modelo y formulario.
        # https://docs.djangoproject.com/en/5.0/ref/forms/validation/#form-and-field-validation
        #
        if formulario.is_valid():

            # Guardar el nuevo producto dentro de la base de datos.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            #
            formulario.save()

            # Redirigir al listado de productos.
            # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
            #
            return redirect('pasteleria_app:listar_productos')

    # Si el usuario solo busca solicitar la pagina, mostrar un formulario vacio.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    else:
        formulario = ProductoForm()

    # RENDER
    # Permite generar una respuesta 'HTML' utilizando como minimo, el 'request' y 'template_name' entregados.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # El argumento opcional 'context' actuara como un diccionario, el cual, nos permitira aacceder al formulario desde el 'HTML' utilizando el nombre 'formulario'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#optional-arguments
    #
    return render(request, 'pasteleria_app/crear.html', {'formulario': formulario})
