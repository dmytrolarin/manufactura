from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path('',MakeTableReservation.as_view(), name='reservation'),
]