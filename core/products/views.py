from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class ProductList(TemplateView):
    template_name = 'productslist.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
# Create your views here.
