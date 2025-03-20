from django.urls import path
from product import views

urlpatterns = [
    # path('', views.view_categories, name='categories-list'),
    # path('', views.ViewCategories.as_view(), name='categories-list'),
    path('', views.CategorieList.as_view(), name='categories-list'),
    path('<int:id>/', views.CategoryDetails.as_view(), name='view-specific-category'),
]
