from django.urls import path,include
# from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet, ProductImageViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewSet, initiate_payment, payment_success, payment_cencel, payment_fail, HasOrderedProducts
from rest_framework_nested import routers
from users.views import DashboardStatsView

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='cart')
router.register('orders', OrderViewSet, basename='orders')

product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
product_router.register('images', ProductImageViewSet, basename='product-image')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

# urlpatterns = router.urls
#Good practice:
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path("payment/initiate/", initiate_payment, name='initiate-payment'),
    path("payment/success/", payment_success, name='payment-success'),
    path("payment/cancel/", payment_cencel, name='payment-cancel'),
    path("payment/fail/", payment_fail, name='payment-fail'),
    path("orders/has_ordered/<int:product_id>/", HasOrderedProducts.as_view()),
    path("data/", DashboardStatsView.as_view(), name="dashboard-data"),
    #Can add custom/extra urls if we need
]

'''
urlpatterns = [
    path('products/', include('product.product_urls')),
    path('categories/', include('product.category_urls'))
]
'''