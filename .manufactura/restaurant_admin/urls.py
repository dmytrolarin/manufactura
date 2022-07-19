from django.urls import path
from .views import *
urlpatterns = [
    path('', redir_login, name = 'restaurant_admin'),
    path('login/', LoginAdmin.as_view(),name='login_admin'),
    path('orders/', orders_page, name='orders'),
    path('orders/<slug:status_slug>/', orders_page),
    path('set_order_status/', set_order_status, name='set_order_status'),
    path('menu_editing/', ShowAllMenu.as_view(),name='all_menu_for_editing'),
    path('menu_editing/<slug:cat_slug>/', ShowCategoryOfDish.as_view(),name='category_for_editing'),
]
