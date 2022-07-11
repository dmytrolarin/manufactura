from django.urls import path
from .views import *
urlpatterns = [
    path('', redir_login),
    path('login/', LoginAdmin.as_view(),name='login_admin'),
    path('orders/', orders_page, name='orders')
]
