from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_product, name='create_product'),
    path('store/', views.product_list, name='product_list'),
    path('agents/', views.agents, name='agents'),
    path('category/', views.product_category, name='product_category'),
    path('category/<str:category_name>/', views.products_by_category, name='products_by_category'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail')
]
