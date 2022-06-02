from django.contrib import admin
from .models import*
# Register your models here.

class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','time_reservation')
    list_display_links = ('id','client_name')
    search_fields = ('id','client_name','time_reservation')
admin.site.register(TableReservation,TableReservationAdmin)
