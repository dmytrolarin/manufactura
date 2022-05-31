from django.contrib import admin
from .models import*
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('id','name')




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
