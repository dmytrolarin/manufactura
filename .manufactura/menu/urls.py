from django.urls import path
from .views import *
urlpatterns = [
    path('', ShowAllMenu.as_view(),name='all_menu'),
    path('<slug:cat_slug>/', ShowCategory.as_view(),name='category'),
]