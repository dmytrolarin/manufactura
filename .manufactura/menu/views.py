from django.shortcuts import render
from django.views.generic import ListView
from .models import*

class ShowAllMenu(ListView):
    model = Product
    template_name = 'menu/menu.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        return context

