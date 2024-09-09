from typing import Any
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model

class Main(generic.TemplateView):
    template_name ='main.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context