from django.shortcuts import render, redirect, get_object_or_404
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


# DETALLE_PRODUCTO
# Vista encargada de consultar y mostrar la informacion de un producto especifico mediante su identificador 'id'.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments
#
def detalle_producto(request, id):

    # GET_OBJECT_OR_404
    # Busca un producto cuyo identificador coincida con el 'id' recibido desde la 'URL', y si es que el producto no existe, 'Django' devuelve una respuesta 'HTTP' '404'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404
    #
    producto = get_object_or_404(Producto, id=id)

    # RENDER
    # Permite generar una respuesta 'HTML' utilizando como minimo, el 'request' y 'template_name' entregados.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # El argumento opcional 'context' actuara como un diccionario, el cual, nos permitira aacceder al producto desde el 'HTML' utilizando el nombre 'producto'.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#optional-arguments
    #
    return render(request, 'pasteleria_app/detalle.html', {'producto': producto})
