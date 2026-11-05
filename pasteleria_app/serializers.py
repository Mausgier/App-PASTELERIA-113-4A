from rest_framework import serializers
from .models import Producto


# Convierte los productos a 'JSON' y valida los datos recibidos.
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

        # Campos obligatorios en las solicitudes 'JSON'.
        extra_kwargs = {
            'nombre': {
                'required': True,
                'allow_blank': False
            },
            'categoria': {
                'required': True
            },
            'precio': {
                'required': True
            },
            'stock': {
                'required': True
            },
        }

    # Validar los tipos originales recibidos desde 'JSON'.
    def to_internal_value(self, data):

        if not isinstance(data, dict):
            raise serializers.ValidationError({
                'non_field_errors': [
                    'Debes enviar un objeto JSON.'
                ]
            })

        errores = {}

        # Los campos textuales deben recibir cadenas.
        for campo in ['nombre', 'descripcion', 'categoria']:
            if campo in data and type(data[campo]) is not str:
                errores[campo] = [
                    'Este campo debe contener texto.'
                ]

        # Precio y stock deben recibir enteros.
        for campo in ['precio', 'stock']:
            if campo in data and type(data[campo]) is not int:
                errores[campo] = [
                    'Este campo debe ser un número entero.'
                ]

        if errores:
            raise serializers.ValidationError(errores)

        return super().to_internal_value(data)

    # Validar nombre.
    def validate_nombre(self, valor):

        nombre = valor.strip()

        if not nombre:
            raise serializers.ValidationError(
                'El nombre no puede estar vacío.'
            )

        return nombre

    # Validar precio.
    def validate_precio(self, valor):

        if valor < 1:
            raise serializers.ValidationError(
                'El precio debe ser mayor o igual a 1.'
            )

        return valor

    # Validar stock.
    def validate_stock(self, valor):

        if valor < 0:
            raise serializers.ValidationError(
                'El stock no puede ser negativo.'
            )

        return valor

