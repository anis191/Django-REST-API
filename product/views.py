from django.shortcuts import get_object_or_404
from django.http import HttpResponse #'HttpResponse' used in django MVT view.
from rest_framework.decorators import api_view #For use a view as a api view,we need this decorators.
from rest_framework.response import Response #'Response' used in DRF view
from product.models import *
from product.serializers import *
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
from drf_yasg.utils import swagger_auto_schema

#This view handel create/retrieve/update/destroy all perform:
class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name','description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()
    '''Note: prefetch_related() is used for reverse relationships or many-to-many'''

    # Here we override  this actions only just show doc string on swagger api gaid
    # List products
    @swagger_auto_schema(
        operation_summary='Browse products',
        operation_description="""
        Return a paginated list of all products.

        - Accessible to all users.
        - Supports filtering by query parameters.
        - Supports full-text search on `name`, `description`, and `category`.
        - Supports ordering by `price` and `updated_at`.
        """
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Create product
    @swagger_auto_schema(
        operation_summary='Create a new product',
        operation_description='Only authenticated admin users are allowed to create a new product.'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # Retrieve single product
    @swagger_auto_schema(
        operation_summary='Retrieve product details',
        operation_description='Returns the details of a specific product by its ID.'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # Update product
    @swagger_auto_schema(
        operation_summary='Update a product',
        operation_description='Fully update a product. Only authenticated admin users are allowed.'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Partially update product
    @swagger_auto_schema(
        operation_summary='Partially update a product',
        operation_description='Partially update fields of a product. Only authenticated admin users are allowed.'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # Delete product
    @swagger_auto_schema(
        operation_summary='Delete a product',
        operation_description='Deletes a product by its ID. Only authenticated admin users are allowed.'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        return[IsAdminUser()]
    """

class ProductImageViewSet(ModelViewSet):
    # queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ProductImage.objects.filter(
            product_id = self.kwargs.get('product_pk')
        )
    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs.get('product_pk'))

#This view handel create/retrieve/update/destroy all perform:
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(
            product_id = self.kwargs.get('product_pk')
        )

    def get_serializer_context(self):
        ''' [We update this line with get() method for solve a error of swagger docs]
        return {'product_id' : self.kwargs['product_pk'],
                'user' : self.request.user}
        '''
        return {'product_id' : self.kwargs.get('product_pk'),
            'user' : self.request.user}
