from django.apps import AppConfig
'''Приложение для меню ресторана'''

class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
    verbose_name = 'Меню'
