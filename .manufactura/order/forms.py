from django import forms
from .models import*

class MakeTableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ('client_name','client_phone_number','date_reservation','time_reservation',
        'amount_persons','order_comment')
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder':"Введіть ваше ім'я"}),
            'client_phone_number': forms.NumberInput(attrs={'placeholder':"+380888888888"}),
            'date_reservation': forms.TextInput(attrs={'placeholder':'01.01'}),
            'time_reservation': forms.TimeInput(attrs={'placeholder':'12:00'}),
            'amount_persons': forms.NumberInput(attrs={'placeholder':'Введіть кілкьість осіб'}),
            'order_comment':forms.Textarea(attrs={'placeholder':"Коментар до замовлення (необов'язково)"})
        }

class MakeTakeAwayForm(forms.ModelForm):
    class Meta:
        model = TakeAway
        fields= ('client_name','client_phone_number','time_cooking',
        'order_comment')
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder':"Введіть ваше ім'я"}),
            'client_phone_number': forms.NumberInput(attrs={'placeholder':"+380888888888"}),
            'time_cooking': forms.TimeInput(attrs={'placeholder':'13:00'}),
            'order_comment':forms.Textarea(attrs={'placeholder':"Коментар до замовлення (необов'язково)"})
        }

class MakeDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('client_name','client_phone_number','adress','time_delivery',
        'order_comment')
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder':"Введіть ваше ім'я"}),
            'client_phone_number': forms.NumberInput(attrs={'placeholder':"+380888888888"}),
            'adress':forms.TextInput(attrs={'placeholder':"вул. Шевченка, буд. 3, кв.40"}),
            'time_delivery': forms.TimeInput(attrs={'placeholder':'13:00'}),
            
            'order_comment':forms.Textarea(attrs={'placeholder':"Коментар до замовлення (необов'язково)"})
        }