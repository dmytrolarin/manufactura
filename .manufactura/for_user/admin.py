from django.contrib import admin
from .models import*

class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('id','rest_email','rest_phone_number','time_working')
    list_display_links = ('id','rest_email','rest_phone_number','time_working')

admin.site.register(RestaurantInfo,RestaurantInfoAdmin)
