
from django.db import models
from django.contrib.auth.models import User


class AdminAdditionalInfo(models.Model):
    ''' В моделе храниться расширенеа информация про админитсратора'''
    admin_account = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Адміністратор')

    CHOICES_RIGTHS = (
        ('order_management','Керування замовленнями'),
        ('menu_editing','Редагування меню'),
        ('rest_info_editing','Редагування інфо про ресторан'),
        ('all_rights','Повні права'),
    )

    rights = models.CharField(max_length=255, choices=CHOICES_RIGTHS, verbose_name='Права')

    class Meta:
        verbose_name = 'Інформація про адмінстратора'
        verbose_name_plural = 'Інформація про адмінстраторів'