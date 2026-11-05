from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Producto
from .serializers import ProductoSerializer


# API REST para listar y crear productos.
class ProductosAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    # GET: Listar todos los productos.
    def get(self, request):

        productos = Producto.objects.all().order_by('id')

        serializer = ProductoSerializer(
            productos,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST: Crear un nuevo producto.
    def post(self, request):

        serializer = ProductoSerializer(
            data=request.data
        )

        # Comprobar los datos recibidos.
        serializer.is_valid(raise_exception=True)

        # Guardar el producto en MySQL.
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


# API REST para consultar, actualizar y eliminar por ID.
class ProductoDetalleAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    # GET: Consultar un producto por ID.
    def get(self, request, id):

        producto = get_object_or_404(Producto, id=id)

        serializer = ProductoSerializer(producto)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # PUT: Actualizar un producto existente.
    def put(self, request, id):

        producto = get_object_or_404(Producto, id=id)

        serializer = ProductoSerializer(
            producto,
            data=request.data
        )

        # Validar los nuevos datos.
        serializer.is_valid(raise_exception=True)

        # Persistir las modificaciones.
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # DELETE: Eliminar un producto existente.
    def delete(self, request, id):

        producto = get_object_or_404(Producto, id=id)

        producto.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

