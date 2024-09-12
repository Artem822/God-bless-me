from django.urls import path
from .views import *
from cart.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path(r'<int:pk>/', Product_info.as_view(), name='product_info'),
    path('add/<int:product_id>/', AddToCart, name='add'),
    path('delete/<int:product_id>/', DeleteFromCart, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    