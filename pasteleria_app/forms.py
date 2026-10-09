from django import forms
from .models import Producto


#
# "PRODUCTOFORM"
# Formulario basado en el modelo 'Producto'.
# https://docs.djangoproject.com/en/5.0/topics/forms/#building-a-form-in-django
#
# 'ModelForm' permite generar campos de formulario a partir de los campos definidos en 'models.py'.
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#creating-forms-from-models
#
class ProductoForm(forms.ModelForm):

    #
    # "META"
    # Clase interna que establece la configuracion del formulario.
    # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#a-full-example
    #
    class Meta:

        #
        # "MODEL"
        # Indica el modelo asociado al formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#a-full-example
        #
        model = Producto

        #
        # "FIELDS"
        # Define los campos del modelo que estaran disponibles en el formulario.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#a-full-example
        #
        fields = [
            'nombre',
            'descripcion',
            'categoria',
            'precio',
            'stock',
        ]

        #
        # "LABELS"
        # Personaliza los nombres visibles de los campos del formulario.
        # Las claves corresponden a los nombres definidos en el modelo 'Producto'.
        # Los valores son las etiquetas que 'Django' mostrara en las plantillas 'HTML'.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#overriding-the-default-fields
        #
        labels = {
            'descripcion': 'Descripción',
            'categoria': 'Categoría',
        }
