from django.db import models

# Модель для резервации столиков
class TableReservation(models.Model):
    client_name = models.CharField(max_length=255,verbose_name="Ім'я клієтна")
    client_phone_number = models.IntegerField(verbose_name="Номер телефону")
    time_reservation = models.TimeField(verbose_name="Час бронювання")
    amount_persons = models.IntegerField(verbose_name="Кількість персон")
    order = models.TextField(blank=True,verbose_name="Замовлення")
    special_requests = models.TextField(blank=True,verbose_name="Особливі побажання")
    def __str__(self):
        return f"{self.client_name}, {self.time_reservation}"

    class Meta:
        verbose_name = 'Бронювання столу'
        verbose_name_plural = 'Бронювання столів'
