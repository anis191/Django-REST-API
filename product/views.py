from django.shortcuts import get_object_or_404
from django.http import HttpResponse #'HttpResponse' used in django MVT view.
#For create rest view we need to import this:
from rest_framework.decorators import api_view #For use a view as a api view,we need this decorators.
from rest_framework.response import Response #'Response' used in DRF view
from product.models import *
from product.serializers import *
from django.db.models import Count
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

#This view handel create/retrieve/update/destroy all perform:
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#This view handel create/retrieve/update/destroy all perform:
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(
            product_id = self.kwargs['product_pk']
        )

    def get_serializer_context(self):
        return {'product_id' : self.kwargs['product_pk']}
