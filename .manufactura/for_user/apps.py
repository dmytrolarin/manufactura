from django.apps import AppConfig
"""Приложение прденазначено для работы со страницами, 
которые несут ифнормацию для пользователя"""

class ForUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'for_user'
    verbose_name = 'Для користувачів'