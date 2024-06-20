from typing import Any
from django.shortcuts import render
from django.views import generic

class Main(generic.TemplateView):
    template_name ='main.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)