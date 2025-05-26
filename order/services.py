from order.models import Cart, CartItem, Order, OrderItem
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError

class OrderServices:
    @staticmethod
    def create_order(user_id, cart_id):
        with transaction.atomic():
            cart = Cart.objects.get(pk=cart_id)
            cart_items = cart.items.select_related('product').all()
    
            total= []
            for item in cart_items:
                total.append(item.product.price * item.quantity)
            total_price = sum(total)
    
            order = Order.objects.create(
                user_id=user_id, total_price=total_price
            )
    
            order_items = [
                OrderItem(
                    order = order,
                    product = item.product,
                    quantity = item.quantity,
                    price = item.product.price,
                    total_price = (item.quantity * item.product.price)
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
    
            cart.delete()
    
            return order
    
    @staticmethod
    def cancel_order(order, user):
        if user.is_staff:
            order.status = Order.CANCELED
            order.save()
            return order
        
        if order.user != user:
            raise PermissionDenied("You can cancel only your own order")
        
        if order.status == Order.DELIVERED:
            raise ValidationError("You can't cancel an order")
        
        order.status = Order.CANCELED
        order.save()
        return order
        
