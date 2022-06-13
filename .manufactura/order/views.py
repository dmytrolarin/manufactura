from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import*
from .forms import*
from django.core.mail import send_mail
from manufactura import settings

# Функция для обработки формы для брони столика
def make_table_reservation(request):
    form = MakeTableReservationForm
    context = {
        'form':form,
        'title':'Бронювання столику',
        'selected':'reservation',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]

    }
    if  request.method == 'POST':
        form = MakeTableReservationForm(request.POST)
        if form.is_valid():
            subject = 'Бронювання столику'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            time_reservation = form.cleaned_data.get('time_reservation')
            amount_persons = form.cleaned_data.get('amount_persons')
            order = form.cleaned_data.get('order')
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number}; 
            \rЧас бронвання: {time_reservation}; 
            \rКількість персон: {amount_persons};
            \rЗамовлення: {order}."""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
    if request.path_info.split('/')[-2] == 'reservation_only':
        context['show_format_choice'] = False
    return render(request, 'order/reservation_form.html', context=context)
    

# Функция для обработки формы для самовывоза 
def make_take_away(request):
    form = MakeTakeAwayForm
    context = {
        'form':form,
        'title':'Самовивіз',
        'selected':'takeaway',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]
    }
    if request.method == 'POST':
        form = MakeTakeAwayForm(request.POST)
        if form.is_valid():
            subject = 'Замовлення на самовивіз'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            time_cooking = form.cleaned_data.get('time_cooking')
            order = form.cleaned_data.get('order')
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number}; 
            \rЧас приготування: {time_cooking}; 
            \rЗамовлення: {order}."""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
    return render(request, 'order/takeaway_form.html', context=context)


# Функция для обработки формы для доставки 
def make_delivery(request):
    form = MakeDeliveryForm
    context = {
        'form':form,
        'title':'Доставка',
        'selected':'delivery',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]
    }
    if request.method == 'POST':
        form = MakeDeliveryForm(request.POST)
        if form.is_valid():
            subject = 'Замовлення на доставку'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            adress = form.cleaned_data.get('adress')
            time_delivery = form.cleaned_data.get('time_delivery')
            order = form.cleaned_data.get('order')
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number};
            \rЧас доставки: {adress}; 
            \rЧас доставки: {time_delivery}; 
            \rЗамовлення: {order}."""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
    return render(request, 'order/delivery_form.html', context=context)