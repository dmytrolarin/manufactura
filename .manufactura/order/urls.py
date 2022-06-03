from django.urls import path
from .views import *
urlpatterns = [
    path('reservation/',MakeTableReservation.as_view(), name='reservation'),
    path('takeaway/',show_form_takeaway, name='takeaway'),
    path('delivery/', show_form_delivery,name='delivery')
]
