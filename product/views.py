from django.shortcuts import get_object_or_404
from django.http import HttpResponse #'HttpResponse' used in django MVT view.
#For create rest view we need to import this:
from rest_framework.decorators import api_view #For use a view as a api view,we need this decorators.
from rest_framework.response import Response #'Response' used in DRF view
from product.models import *
from product.serializers import *
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

'''
# This is a normal Django MVT view (not an API view):

def view_products(request):
    return HttpResponse("Okey")
'''

# This is a DRF-based API view:(Function-based View)
'''
@api_view(['GET','PUT','DELETE'])
def view_specific_products(request, id):
    # product = Product.objects.get(pk = id)
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)  #Syntax-->(ModelName, condition)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT': #This is useally Update operation
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
#Class-based Views
'''
class ViewSpecificProducts(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)  #Syntax-->(ModelName, condition)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
#Generics API View:
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    #Here we customize a method of "RetrieveUpdateDestroyAPIView" call "delete()" for add our logic.
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.stock > 10:
            return Response({'message':"Product with stock more than 10 could not be delete!"})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Function-based Views
'''
@api_view(['GET','POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)   #Deserializer
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
#Class-based Views
'''
class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)   #Deserializer
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
#Generics API View:
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    
    """
    We use get_queryset() and get_serializer_class() methods when we need to return 
    data (queryset/serializer class) based on certain conditions, such as user type. 
    Otherwise, we can define them directly as attributes (queryset, serializer_class, etc.).

    def get_queryset(self):
        products = Product.objects.select_related('category').all()
        return products
    
    def get_serializer_class(self):
        #Just return only the def serializer model class
        return ProductSerializer
    """

#Function-based Views
'''
@api_view()
def view_categories(request):
    categories = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
'''
#Class-based Views
'''
class ViewCategories(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)   #Deserializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
#Generics API View:
class CategorieList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer

#Function-based Views
'''
@api_view()
def view_specific_category(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
'''
#Class-based Views
'''
class ViewSpecificCategory(APIView):
    def get(self, request, id):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')).all(),
            pk=id
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')).all(),
            pk=id
        )
        serializer = CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
#Generics API View:
class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
