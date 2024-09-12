from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product
from cart.models import Cart

class ProductList(TemplateView):
    template_name = 'productslist.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
class Product_info(TemplateView):
    def get(self, request, pk):
        template_name = 'product_info.html'
        product = Product.objects.get(pk=pk)
        try:
            user_products = Cart.objects.get(user=request.user)
        except:
            user_products = None
        context = {"product":product,
                   "user_products":user_products}
        return render(request, template_name, context)

    

