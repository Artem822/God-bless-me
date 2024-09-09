from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Cart
from django.contrib.auth.models import User

class CartList(generic.TemplateView):
    def get(self, request):
        context = {'cart_items':Cart.objects.get(user=request.user)}
        return render(request, 'cartlist.html', context)