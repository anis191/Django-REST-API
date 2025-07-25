from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.serializers import *
from order.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from order.services import OrderServices

class CartViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet, RetrieveModelMixin):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Add this getatter() method only for solve a swagger docs error:
        if getattr(self, 'swagger_fake_view',False):
            return Cart.objects.none()
        return Cart.objects.filter(
            user = self.request.user
        ).prefetch_related('items__product')
    
    def create(self, request, *args, **kwargs):
        existing_cart = Cart.objects.filter(user = request.user).first()
        if existing_cart:
            serializer = self.get_serializer(existing_cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)


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
        if getattr(self, 'swagger_fake_view',False):
            return CartItem.objects.none()

        return CartItem.objects.select_related('product').filter(cart_id = self.kwargs.get('cart_pk'), cart__user = self.request.user)
    
    def get_serializer_context(self):
        # Add this getatter() method only for solve a swagger docs error:
        context = super().get_serializer_context()
        if getattr(self, 'swagger_fake_view', False):
            return context

        return {'cart_id' : self.kwargs.get('cart_pk')}

class OrderViewSet(ModelViewSet):
    http_method_names = ['get','post','delete','patch','head','options']
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    # Here we implament a django action for cancel an order:
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        OrderServices.cancel_order(order=order, user=request.user)
        return Response({'status' : 'Order Canceled'})
    
    # Here we implament a django action for admin update an order status:
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        serializer = UpdateOrderSerializers(
            order, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status' : 'Order status updated'})

    def get_permissions(self):
        # if self.request.method == 'DELETE':
        if self.action in ['update_status', 'destroy','partial_update']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializers
        # if self.request.method == 'POST':
        if self.action == 'create':
            return CreateOrderSerializers
        # elif self.request.method == 'PATCH':
        # elif self.action == 'update_status':
        elif self.action in ['update_status','partial_update']:
            return UpdateOrderSerializers
        return OrderSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view',False):
            return Order.objects.none()

        if self.request.user.is_staff is True:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(
            user = self.request.user
        )
    
    def get_serializer_context(self):
        if getattr(self, 'swagger_fake_view',False):
            return super().get_serializer_context()
        return {'user_id' : self.request.user.id, 'user':self.request.user}
    