from rest_framework import serializers
from decimal import Decimal
from product.models import *

'''
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
'''
class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id","name","description","product_count"]

    # product_count = serializers.IntegerField()

"""
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    # Add custom field:
    after_discount = serializers.SerializerMethodField(method_name='discount')
    '''category = serializers.PrimaryKeyRelatedField(
        #It get all categories of this product
        queryset = Category.objects.all()
    )'''
    #Show the product category name
    # category = serializers.StringRelatedField()

    #Show the product category with details as nested
    category = CategorySerializer()

    def discount(self, product):
        price = product.price - (product.price * Decimal(0.10))
        return round(price, 2)
"""

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__' #For all model fields
        fields = ["id","name","description","price","stock","category","after_discount"]
    
    # Add extra fields(if we need):
    after_discount = serializers.SerializerMethodField(method_name='discount')
    def discount(self, product):
        price = product.price - (product.price * Decimal(0.10))
        return round(price, 2)
    
    #Field Validation:
    def validate_price (self, price):
        if price < 0:
            raise serializers.ValidationError("Price Can't be negative")
        return price
