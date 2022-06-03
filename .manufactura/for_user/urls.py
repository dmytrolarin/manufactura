from .views import*
from django.urls import path
urlpatterns = [
    path('about_us/',show_about_us, name='about_us'),
    path('contacts/',show_contacts, name='contacts'),
    path('review/',show_review_form,name='review_form')
]