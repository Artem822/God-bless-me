from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Cart
from products.models import Product

class CartList(generic.TemplateView):
    def get(self, request):
        try:
            Cart.objects.get(user=request.user)
        except:
            Cart.objects.create(user=request.user)
        context = {'cart_items':Cart.objects.get(user=request.user)}
        return render(request, 'cartlist.html', context)
    
def AddToCart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        try:
            user_cart = Cart.objects.get(user=request.user)
            user_cart.product.add(product)
        except:
            cart = Cart.objects.create(user=request.user)
            cart.product.add(product)
    return redirect('products_list')

def DeleteFromCart(request, product_id):
    if request.method == 'POST':
        products_from_cart = Cart.objects.all()[0]
        product = Product.objects.get(pk=product_id)

        products_from_cart.product.remove(product)

        return redirect('cart')
    
 