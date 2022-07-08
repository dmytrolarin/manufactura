from django.db import models
class TableReservation(models.Model):
    '''Модель для бронирования столиков'''
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.CharField(verbose_name="Номер телефону",max_length=13)
    date_reservation = models.DateField(verbose_name='Дата бронювання', max_length=255)
    time_reservation = models.TimeField(verbose_name="Час бронювання", max_length=255)
    amount_persons = models.IntegerField(verbose_name="Кількість персон")
    order = models.TextField(verbose_name="Замовлення",default='Замовлення в закладі')
    order_comment = models.TextField(blank=True,verbose_name="Кометнар до замовлення",)
    total_price = models.IntegerField(verbose_name='Вартість замовлення',default=0)
    def __str__(self):
        return f"{self.client_name}, {self.date_reservation}, {self.time_reservation}"  
    class Meta:
        verbose_name = 'Бронювання столу'
        verbose_name_plural = 'Бронювання столиків'

class TakeAway(models.Model):
    '''Модель для оформления заказов форматом самовывоза'''
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.CharField(verbose_name="Номер телефону",max_length=13)
    time_cooking = models.TimeField(verbose_name="Час приготування")
    order = models.TextField(verbose_name="Замовлення")
    order_comment = models.TextField(verbose_name="Коментар до замовлення",blank=True)
    total_price = models.IntegerField(verbose_name='Вартість замовлення')

    def __str__(self):
        return f"{self.client_name}, {self.time_cooking}"

    class Meta:
        verbose_name = 'Самовивіз'
        verbose_name_plural = 'Самовивози'



# class Delivery(models.Model):
#     '''Модель для оформления заказов форматом доставки'''
#     client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
#     client_phone_number = models.CharField(verbose_name="Номер телефону", max_length=13)
#     adress = models.TextField(verbose_name="Адреса доставки")
#     time_delivery = models.TimeField(verbose_name="Час доставки")
#     order_comment = models.TextField(verbose_name="Коментар до замовлення",blank=True)

#     def __str__(self):
#         return f"{self.client_name}, {self.time_delivery}, {self.adress}"

#     class Meta:
#         verbose_name = 'Доставка'
#         verbose_name_plural = 'Доставки'

