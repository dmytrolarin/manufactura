from django.urls import path
from .views import *
urlpatterns = [
    path('', ShowAllMenu.as_view(),name='all_menu')
]