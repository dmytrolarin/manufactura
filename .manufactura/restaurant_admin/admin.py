from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import*
class AdminAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('id','admin_account','rights')
    list_display_links = ('id','admin_account','rights')
    search_fields = ('admin_account','rights')






admin.site.register(AdminAdditionalInfo,AdminAdditionalInfoAdmin)

