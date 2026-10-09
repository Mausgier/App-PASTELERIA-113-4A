from django.db import models
from django.core.validators import MinValueValidator


#
# PRODUCTO
# Modelo principal que se utilizara para poder gestionar los productos dentro de la aplicacion 'pasteleria_app'.
# https://docs.djangoproject.com/en/5.0/topics/db/models/#module-django.db.models
#
class Producto(models.Model):

    #
    # NOMBRE
    # Variable textual de caracter obligatorio.
    #
    # 'CharField' corresponde a un campo diseñado para almacenar texto de manera limitada.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield
    #
    # 'max_length=100' establece que este campo puede poseer hasta un maximo de '100' caracteres.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField.max_length
    #
    nombre = models.CharField(
        max_length=100
    )

    #
    # DESCRIPCION
    # Variable textual de caracter opcional.
    #
    # 'TextField' corresponde a un campo diseñado para almacenar texto de manera extensa.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#textfield
    #
    # 'blank=True' establece que este campo puede estar vacio.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#blank
    #
    descripcion = models.TextField(
        blank=True
    )

    #
    # CATEGORIA
    # Variable textual de caracter obligatorio.
    #
    # 'CharField' corresponde a un campo diseñado para almacenar texto de manera limitada.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield
    #
    # 'max_length=20' establece que este campo puede poseer hasta un maximo de '20' caracteres.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField.max_length
    #
    # 'choices' se asegura de crear opciones y asignar a cada una un nombre legible, para luego, encargar a 'Django' a que este valide los valores entregados.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    #
    # Cabe mencionar que para validar 'choices' existen dos opciones, o hacer uso de un 'ModelForm', o ejecutar 'full_clean()'.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#validating-objects
    #
    # 'default' se asegura de que al no haber una seleccion, se escoga por defecto la opcion 'otro'.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#default
    #
    categoria = models.CharField(
        max_length=20,
        choices=[
            ('torta', 'Torta'),
            ('pastel', 'Pastel'),
            ('galleta', 'Galleta'),
            ('otro', 'Otro'),
        ],
        default='otro'
    )

    #
    # PRECIO
    # Variable numerica de caracter obligatorio.
    #
    # 'DecimalField' corresponde a un campo numerico decimal.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield
    #
    # 'max_digits=10' limita la maxima cantidad de digitos que un numero puede poseer a '10' digitos.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DecimalField.max_digits
    #
    # 'decimal_places=0' limita la cantidad de digitos decimales que un numero puede poseer a '0' digitos.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DecimalField.decimal_places
    #
    # 'validators' se encarga de realizar todas las validaciones que se especifiquen dentro de su campo.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#validators
    #
    # '[MinValueValidator(1)]' es un metodo de validacion, el cual, en nuestro caso, comprobara que cualquier valor que se ingrese sea mayor o igual a '1'.
    # https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator
    #
    # Cabe mencionar que el metodo de validacion 'MinValueValidator' retornara como error 'ValidationError', el cual, es una de las muchas excepciones contenidas por 'Django'.
    # https://docs.djangoproject.com/en/5.0/ref/exceptions/#validationerror
    #
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        validators=[MinValueValidator(1)]
    )

    #
    # STOCK
    # Variable numerica de caracter obligatorio.
    #
    # 'PositiveIntegerField' corresponde a un campo numerico, el cual, debe de ser o un valor positivo o '0'.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#positiveintegerfield
    #
    # 'default' se asegura de que al no haber una seleccion, se escoga por defecto la opcion '0'.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#default
    #
    stock = models.PositiveIntegerField(
        default=0
    )

    # Funcion que retorna el nombre del producto.
    def __str__(self):
        return self.nombre
