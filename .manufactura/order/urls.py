from django.urls import path
from .views import *
urlpatterns = [
    path('reservation/',MakeTableReservation.as_view(), name='reservation'),
]
