from django.urls import path
from product import views

urlpatterns = [
    # path('', views.view_products, name='view-products'),
    # path('', views.ViewProducts.as_view(), name='view-products'),
    path('', views.ProductList.as_view(), name='view-products'),
    # path('<int:id>/', views.ViewSpecificProducts.as_view(), name='view-specific-product'),
    path('<int:id>/', views.ProductDetails.as_view(), name='view-specific-product'),
]
