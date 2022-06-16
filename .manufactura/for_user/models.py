from statistics import mode
from django.db import models

class RestaurantInfo(models.Model):
    '''Модель для информации о ресторане, которая может изменяться'''
    rest_phone_number = models.IntegerField(verbose_name='Номер телефону ресторану')
    time_working = models.CharField(verbose_name='Час роботи', max_length=255)

    def __str__(self):
        return 'Інформація про ресторан'
        
    class Meta:
        verbose_name = 'Інформація про ресторан'
        verbose_name_plural = 'Інформація про ресторан'

class SliderContent(models.Model):
    '''Модель для картинок слайдера'''
    slide_name = models.CharField(max_length=255,verbose_name="Ім'я слайдера")
    photo = models.ImageField(upload_to = "photos/slider",verbose_name='Зображення для слайдера')
    def __str__(self):
        return self.slide_name

    class Meta:
        verbose_name = 'Контент слайдера'
        verbose_name_plural = 'Контент слайдера'