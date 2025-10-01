from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Count, Sum, Avg, Q, Value, IntegerField, DecimalField
from django.db.models.functions import Coalesce

from product.models import Category, Product, Review
from order.models import Order, OrderItem
from users.models import User


class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {}

        # Decimal Value for totals (match your Order.total_price DecimalField)
        decimal_zero = Value(0, output_field=DecimalField(max_digits=10, decimal_places=2))
        int_zero = Value(0, output_field=IntegerField())

        if user.is_staff:
            # Single DB query for order-related aggregates
            order_aggs = Order.objects.aggregate(
                total_orders=Count('id'),
                total_payments=Coalesce(
                    Sum('total_price', filter=~Q(status=Order.NOT_PAID)),
                    decimal_zero
                ),
                pending_payments=Coalesce(
                    Sum('total_price', filter=Q(status=Order.NOT_PAID)),
                    decimal_zero
                ),
                total_revenue=Coalesce(
                    Sum('total_price', filter=Q(status=Order.DELIVERED)),
                    decimal_zero
                ),
                total_refunds=Coalesce(
                    Sum('total_price', filter=Q(status=Order.CANCELED)),
                    decimal_zero
                ),
            )

            data = {
                "total_categories": Category.objects.count(),
                "total_products": Product.objects.count(),
                "total_orders": order_aggs['total_orders'] or 0,
                "total_users": User.objects.count(),
                "total_reviews": Review.objects.count(),
                # avg_rating is integer/float — simple safe fallback
                "avg_rating": Review.objects.aggregate(avg=Avg('ratings'))['avg'] or 0,
                "total_payments": order_aggs['total_payments'],
                "pending_payments": order_aggs['pending_payments'],
                "total_revenue": order_aggs['total_revenue'],
                "total_refunds": order_aggs['total_refunds'],
            }

        else:
            # Aggregate orders for this user in a single DB query
            user_order_aggs = Order.objects.filter(user=user).aggregate(
                total_orders=Count('id'),
                total_payments=Coalesce(
                    Sum('total_price', filter=~Q(status=Order.NOT_PAID)),
                    decimal_zero
                ),
                pending_payments=Coalesce(
                    Sum('total_price', filter=Q(status=Order.NOT_PAID)),
                    decimal_zero
                ),
            )

            # OrderItem aggregation for delivered purchased products (quantity is integer)
            purchase_products = OrderItem.objects.filter(
                order__user=user, order__status=Order.DELIVERED
            ).aggregate(total_products=Coalesce(Sum('quantity'), int_zero))['total_products']

            data = {
                "purchase_products": purchase_products,
                "total_orders": user_order_aggs['total_orders'] or 0,
                "total_payments": user_order_aggs['total_payments'],
                "pending_payments": user_order_aggs['pending_payments'],
            }

        return Response(data)