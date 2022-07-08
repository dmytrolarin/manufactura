from django import forms
from .models import*

class MakeTableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ('client_name','client_phone_number','date_reservation','time_reservation',
        'amount_persons','order_comment')
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder':"Введіть ваше ім'я"}),
            'client_phone_number': forms.NumberInput(attrs={'placeholder':"+380888888888",'type':'tel'}),
            'date_reservation': forms.TextInput(attrs={'placeholder':'01.01', 'type':'date'}),
            'time_reservation': forms.TimeInput(attrs={'placeholder':'12:00','type':'time'}),
            'amount_persons': forms.NumberInput(attrs={'placeholder':'Введіть кілкьість персон'}),
            'order_comment':forms.Textarea(attrs={'placeholder':"Коментар до замовлення (необов'язково)"})
        }

class MakeTakeAwayForm(forms.ModelForm):
    class Meta:
        model = TakeAway
        fields= ('client_name','client_phone_number','time_cooking',
        'order_comment')
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder':"Введіть ваше ім'я"}),
            'client_phone_number': forms.NumberInput(attrs={'placeholder':"+380888888888",'type':'tel'}),
            'time_cooking': forms.TimeInput(attrs={'placeholder':'13:00','type':'time'}),
            'order_comment':forms.Textarea(attrs={'placeholder':"Коментар до замовлення (необов'язково)"})
        }

# 
    