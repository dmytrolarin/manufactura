from django.contrib import admin
from .models import*

class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('rest_phone_number','time_working')
    list_display_links = ('rest_phone_number','time_working')

class SliderContentAdmin(admin.ModelAdmin):
    list_display = ('slide_name',)
    list_display_links = ('slide_name',)

admin.site.register(RestaurantInfo,RestaurantInfoAdmin)
admin.site.register(SliderContent,SliderContentAdmin)
