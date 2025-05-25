from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.serializers import *
from order.models import *
from rest_framework.permissions import IsAuthenticated

class CartViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet, RetrieveModelMixin):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(
            user = self.request.user
        )

class CartItemViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id = self.kwargs['cart_pk'], cart__user = self.request.user)
    
    def get_serializer_context(self):
        return {'cart_id' : self.kwargs['cart_pk']}

class OrderViewSet(ModelViewSet):
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializers
        return OrderSerializer

    def get_queryset(self):
        if self.request.user.is_staff is True:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(
            user = self.request.user
        )
    
    def get_serializer_context(self):
        return {'user_id' : self.request.user.id}
    