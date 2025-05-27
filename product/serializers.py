from rest_framework import serializers
from decimal import Decimal
from product.models import *
from users.models import User

'''
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
'''
class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True, help_text='Return the total number of product in this category')

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

class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializers(many=True, read_only=True)
    class Meta:
        model = Product
        # fields = '__all__' #For all model fields
        fields = ["id","name","description","price","stock","category","after_discount","images"]
    
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

class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name'
    )
    class Meta:
        model = User
        fields = ['id','name']
    
    def get_current_user_name(self, obj):
        return obj.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id','product','ratings','comment','user']
        read_only_fields = ['user','product']
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        user = self.context['user']
        review = Review.objects.create(product_id=product_id,user=user, **validated_data)
        return review
