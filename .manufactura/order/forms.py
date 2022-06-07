from django import forms
from .models import*

class MakeTableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ('client_name','client_phone_number','time_reservation',
        'amount_persons','order')

class MakeTakeAwayForm(forms.ModelForm):
    class Meta:
        model = TakeAway
        fields= ('client_name','client_phone_number','time_cooking',
        'order')

class MakeDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('client_name','client_phone_number','adress','time_delivery',
        'order')