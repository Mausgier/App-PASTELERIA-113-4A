from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


# INICIO
# Vista encargada de mostrar la pagina principal de la aplicacion de pasteleria 'pasteleria_app'.
#
def inicio(request):

    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/inicio.html'.
    #
    return render(request, 'pasteleria_app/inicio.html')


# LISTAR_PRODUCTOS
# Vista encargada de mostrar la pagina responsable de permitir el poder consultar y mostrar los productos almacenados dentro de la base de datos.
#
def listar_productos(request):

    # PRODUCTO.OBJECTS.ALL()
    # Obtiene todos los registros del modelo 'Producto' mediante las funciones de 'Django'.
    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-all-objects
    #
    productos = Producto.objects.all()

    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/lista.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'productos'.
    #
    return render(request, 'pasteleria_app/lista.html', {'productos': productos})


# CREAR_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir recibir, validar y guardar nuevos productos dentro de la base de datos.
#
def crear_producto(request):

    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        # Crear una instancia del formulario utilizando los datos especificados.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
        #
        # 'request.POST' corresponde a los datos entregados por el 'POST'.
        #
        formulario = ProductoForm(request.POST)

        # Comprobar que los datos cumplan con las validaciones definidas dentro de nuestro modelo y formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#validation-on-a-modelform
        #
        if formulario.is_valid():

            # Guardar el nuevo producto dentro de la base de datos.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            #
            formulario.save()

            # Redirigir a la pagina de listado de productos.
            # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
            #
            return redirect('pasteleria_app:listar_productos')

    # Si el usuario solo busca solicitar la pagina, mostrar un formulario vacio.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    else:
        formulario = ProductoForm()

    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/crear.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'formulario'.
    #
    return render(request, 'pasteleria_app/crear.html', {'formulario': formulario})


# DETALLE_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir el poder consultar y mostrar la informacion de un producto especifico mediante su identificador 'id'.
#
def detalle_producto(request, id):

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

    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/detalle.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, el unico valor es 'producto'.
    #
    return render(request, 'pasteleria_app/detalle.html', {'producto': producto})


# EDITAR_PRODUCTO
# Vista encargada de mostrar la pagina responsable de permitir consultar, validar y actualizar la informacion de un producto existente.
#
def editar_producto(request, id):

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

    # Comprobar si es que el usuario envio el formulario.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    if request.method == 'POST':

        # Crear una instancia del formulario utilizando los datos especificados.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
        #
        # 'request.POST' corresponde a los datos entregados por el 'POST'.
        # 'instance=producto' indica que se editara un producto existente en vez de generar un producto nuevo.
        #
        formulario = ProductoForm(request.POST, instance=producto)

        # Comprobar que los datos cumplan con las validaciones definidas dentro de nuestro modelo y formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#validation-on-a-modelform
        #
        if formulario.is_valid():

            # Actualizar los datos del producto existente dentro de la base de datos.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
            #
            formulario.save()

            # Redirigir a la pagina de detalle de producto.
            # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
            #
            return redirect('pasteleria_app:detalle_producto', id=producto.id)

    # Si el usuario solo busca solicitar la pagina, mostrar el formulario con sus datos actuales.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    #
    else:
        formulario = ProductoForm(instance=producto)

    # RENDER
    # Genera un objeto de clase 'HttpResponse' a partir de los argumentos que se le entreguen.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    #
    # 'request' corresponde al objeto utilizado para generar la respuesta.
    # 'template_name' corresponde al nombre de la plantilla a utilizar. En este caso, la plantilla es 'pasteleria_app/editar.html'.
    # 'context' corresponde a un diccionario de valores que añade contexto a la plantilla. En este caso, los valores son 'formulario' y 'producto'.
    #
    return render(request,'pasteleria_app/editar.html',{'formulario': formulario,'producto': producto})
