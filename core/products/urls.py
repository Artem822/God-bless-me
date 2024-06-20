from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path(r'<int:pk>/', Product_info.as_view(), name='product_info')
]
