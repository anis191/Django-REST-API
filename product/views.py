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

#This view handel create/retrieve/update/destroy all perform:
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name','description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [DjangoModelPermissions]

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
            product_id = self.kwargs['product_pk']
        )
    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs['product_pk'])

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
            product_id = self.kwargs['product_pk']
        )

    def get_serializer_context(self):
        return {'product_id' : self.kwargs['product_pk'],
                'user' : self.request.user}
