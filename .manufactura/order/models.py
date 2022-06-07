from django.core.mail import send_mail
from for_user.models import RestaurantInfo
# Create your models here.
from django.db import models

class TableReservation(models.Model):
    '''Модель для бронирования столиков'''
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.IntegerField(verbose_name="Номер телефону")
    time_reservation = models.TimeField(verbose_name="Час бронювання")
    amount_persons = models.IntegerField(verbose_name="Кількість персон")
    order = models.TextField(blank=True,verbose_name="Замовлення")
    def __str__(self):
        return f"{self.client_name}, {self.time_reservation}"

  
        
    class Meta:
        verbose_name = 'Бронювання столу'
        verbose_name_plural = 'Бронювання столиків'

class TakeAway(models.Model):
    '''Модель для оформления заказов форматом самовывоза'''
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.IntegerField(verbose_name="Номер телефону")
    time_cooking = models.TimeField(verbose_name="Час приготування")
    order = models.TextField(verbose_name="Замовлення")

    def __str__(self):
        return f"{self.client_name}, {self.time_cooking}"

    class Meta:
        verbose_name = 'Самовивіз'
        verbose_name_plural = 'Самовивози'



class Delivery(models.Model):
    '''Модель для оформления заказов форматом доставки'''
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.IntegerField(verbose_name="Номер телефону")
    adress = models.TextField(verbose_name="Адреса доставки")
    time_delivery = models.TimeField(verbose_name="Час доставки")
    order = models.TextField(verbose_name="Замовлення")

    def __str__(self):
        return f"{self.client_name}, {self.time_delivery}, {self.adress}"

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

