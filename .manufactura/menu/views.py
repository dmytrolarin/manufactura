from django.shortcuts import render
from django.views.generic import ListView, CreateView
from for_user.models import RestaurantInfo

from .models import*
categories = [
            Category.objects.get(slug='snacks'),
            Category.objects.get(slug='soups'),
            Category.objects.get(slug='salads'),
            Category.objects.get(slug='main_dish')
        ]
# def get_amount_product(request):
#     amount_all_products = 0  
#     for cookie_key in list(request.COOKIES):
#         if cookie_key != 'sessionid' and cookie_key != 'csrftoken':
#             amount_all_products += int(request.COOKIES[cookie_key].split()[-1])
#     return amount_all_products
# Для показа всех блюд
class ShowAllMenu(ListView):
    model = Product
    template_name = 'menu/menu.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        context['category_selected'] = 0
        context['rest_info'] = RestaurantInfo.objects.all()[0]
        context['path_pref'] = '../'
        context['showing_all_menu'] = True
        # context['amount_product_in_cart'] = get_amount_product(self.request)
        

        context['categories'] = categories
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
        context['categories']= categories
        context['rest_info'] = RestaurantInfo.objects.all()[0]
        context['path_pref'] = '../../'
        return context

