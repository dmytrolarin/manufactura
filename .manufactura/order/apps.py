from django.apps import AppConfig
'''Приложение для форм, предназначеных для оформления заказа'''

class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'
    verbose_name = 'Замовлення'
