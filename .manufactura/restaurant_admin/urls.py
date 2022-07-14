from django.urls import path
from .views import *
urlpatterns = [
    path('', redir_login),
    path('login/', LoginAdmin.as_view(),name='login_admin'),
    path('orders/', orders_page, name='orders'),
    path('orders/<slug:status_slug>/', orders_page),
    # path('set_order_active_status/', set_order_active_status, name='set_order_active_status')
]
