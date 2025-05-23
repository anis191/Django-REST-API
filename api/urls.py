from django.urls import path,include
# from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet
from rest_framework_nested import routers

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', ReviewViewSet, basename='product-review')

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

    #Can add custom/extra urls if we need
]

'''
urlpatterns = [
    path('products/', include('product.product_urls')),
    path('categories/', include('product.category_urls'))
]
'''