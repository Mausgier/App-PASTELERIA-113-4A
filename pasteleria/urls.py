"""
URL configuration for pasteleria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# URLPATTERNS
# Define las rutas correspondientes a la aplicacion 'pasteleria_app'.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/#url-dispatcher
#
urlpatterns = [
    # ADMIN
    # Corresponde a la ruta de administracion predeterminada por 'Django'.
    #
    path('admin/', admin.site.urls),
    # PASTELERIA_APP
    # Corresponde a todas las rutas definidas dentro de 'pasteleria_app/urls.py'.
    #
    path('', include('pasteleria_app.urls')),
]
