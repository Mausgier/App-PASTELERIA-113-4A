from rest_framework import serializers
from .models import Producto


# Convierte los objetos 'Producto' a 'JSON' y viceversa.
class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto

        fields = [
            'id',
            'nombre',
            'descripcion',
            'categoria',
            'precio',
            'stock',
        ]

        read_only_fields = ['id']

