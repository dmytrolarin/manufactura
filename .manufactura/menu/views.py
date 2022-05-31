from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import*
# Для показа всех блюд
class ShowAllMenu(ListView):
    model = Product
    template_name = 'menu/menu.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        context['category_selected'] = 0
        context['categories']=Category.objects.all()
        return context

# Для показа блюд конкретной категории
class ShowCategory(ListView):
    model = Product
    template_name = 'menu/menu.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.filter(cat__slug = self.kwargs['cat_slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug = self.kwargs['cat_slug'])
        context['title'] = c.name
        context['category_selected'] = c.pk
        context['categories']=Category.objects.all()
        return context

