from django.urls import path
from .views import *
from cart.views import *
urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path(r'<int:pk>/', Product_info.as_view(), name='product_info'),
    path('add/<int:product_id>/', AddToCart, name='add'),
    path('delete/<int:product_id>/', DeleteFromCart, name='delete'),
]
