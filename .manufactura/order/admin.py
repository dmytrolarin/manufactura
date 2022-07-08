from django.contrib import admin
from .models import*
# Register your models here.

class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','time_reservation')
    list_display_links = ('id','client_name')
    search_fields = ('id','client_name')

class TakeAwayAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','time_cooking')
    list_display_links = ('id','client_name')
    search_fields = ('id','client_name')

# class DeliveryAdmin(admin.ModelAdmin):
#     list_display = ('id','client_name','time_delivery','adress')
#     list_display_links = ('id','client_name')
#     search_fields = ('id','client_name')

admin.site.register(TableReservation,TableReservationAdmin)
admin.site.register(TakeAway,TakeAwayAdmin)
# admin.site.register(Delivery,DeliveryAdmin)
