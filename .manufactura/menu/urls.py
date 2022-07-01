from django.urls import path
from .views import *
urlpatterns = [
    path('', ShowAllMenu.as_view(),name='all_menu'),
    path('<slug:cat_slug>/', ShowCategory.as_view(),name='category'),
    path('add_to_cart',add_to_cart,name='add_to_cart')
]