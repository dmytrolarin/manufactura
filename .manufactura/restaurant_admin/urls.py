from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginAdmin.as_view(),name='login_admin'),
    path('orders/', orders_page, name='orders')
]
