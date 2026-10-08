from django.urls import path
from . import views


# APP_NAME
# Define el nombre de la aplicacion como 'pasteleria_app'.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/#url-namespaces-and-included-urlconfs
#
app_name = 'pasteleria_app'


# URLPATTERNS
# Define las rutas correspondientes a la aplicacion 'pasteleria_app'.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/#url-dispatcher
#
urlpatterns = [
    # INICIO
    # Ruta asociada a la funcion 'inicio' definida en 'views.py'.
    #
    # Esta vista se encarga de la pagina de inicio.
    #
    path('', views.inicio, name='inicio'),
    # LISTAR_PRODUCTOS
    # Ruta asociada a la funcion 'listar_productos' definida en 'views.py'.
    #
    # Esta vista se encarga de la pagina responsable de permitir la consulta y muestra de los productos almacenados dentro de la base de datos 'MySQL' / 'MariaDB'.
    #
    path('productos/', views.listar_productos, name='listar_productos'),
    # CREAR_PRODUCTO
    # Ruta asociada a la funcion 'crear_producto' definida en 'views.py'.
    #
    # Esta vista se encarga de la pagina responsable de permitir acceder a un formulario para poder registrar nuevos productos.
    #
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    # DETALLE_PRODUCTO
    # Ruta asociada a la funcion 'detalle_producto' definida en 'views.py'.
    #
    # Esta vista se encarga de la pagina responsable de permitir recibir el identificador 'id' del producto que se desea consultar.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters
    #
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),
    # EDITAR_PRODUCTO
    # Ruta asociada a la funcion 'editar_producto' definida en 'views.py'.
    #
    # Esta vista se encarga de la pagina responsable de permitir identificar y editar un producto existente mediante su 'id'.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters
    #
    path('productos/<int:id>/editar/', views.editar_producto, name='editar_producto'),
]
