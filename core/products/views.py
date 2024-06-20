from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class ProductList(TemplateView):
    template_name = 'productslist.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
class Product_info(TemplateView):
    template_name = 'product_info.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        pk=kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(pk=pk)
        return context
    
# Create your views here.
