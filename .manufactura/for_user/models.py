from django.db import models

class RestaurantInfo(models.Model):
    '''Модель хранит в себе информацию о ресторане, которая может изменяться'''
    rest_email = models.EmailField(verbose_name='Електронна адреса ресторану')
    rest_phone_number = models.IntegerField(verbose_name='Номер телефону ресторану')
    time_working = models.CharField(verbose_name='Час роботи', max_length=255)

    def __str__(self):
        return 'Інформація про ресторан'
        
    class Meta:
        verbose_name = 'Інформація про ресторан'
        verbose_name_plural = 'Інформація про ресторан'