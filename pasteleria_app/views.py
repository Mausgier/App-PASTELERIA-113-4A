from django.shortcuts import render
from .models import Producto


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
