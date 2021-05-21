from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product = Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price']
        )
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        if request.data['name'] is not '':
            product.name = request.data['name']
        if request.data['description'] is not '':
            product.description = request.data['description']
        if request.data['price'] is not '':
            product.price = request.data['price']
        product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response('Product removed')