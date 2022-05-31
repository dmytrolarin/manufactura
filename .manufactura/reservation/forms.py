from django import forms
from .models import*
# Форма для резервирования
class MakeTableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ('client_name','client_phone_number','time_reservation',
        'amount_persons','order','special_requests')