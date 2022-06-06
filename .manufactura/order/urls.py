from django.urls import path
from .views import *
urlpatterns = [
    path('reservation/',MakeTableReservation.as_view(), name='reservation'),
    path('reservation_only/',MakeTableReservation.as_view(), name='reservation_only'),
    path('takeaway/',MakeTakeAway.as_view(), name='takeaway'),
    path('delivery/', MakeDelivery.as_view(),name='delivery')
]
