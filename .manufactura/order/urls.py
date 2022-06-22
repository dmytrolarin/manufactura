from django.urls import path
from .views import *
urlpatterns = [
    path('reservation/',make_table_reservation, name='reservation'),
    path('reservation_only/',make_table_reservation, name='reservation_only'),
    path('takeaway/',make_take_away, name='takeaway'),
    path('delivery/', make_delivery,name='delivery'),
    # path('add_to_cart/', add_to_cart ,name='add_to_cart'),
]
